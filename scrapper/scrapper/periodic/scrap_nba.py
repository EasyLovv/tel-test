import datetime
import re
import json
import asyncio

import aiohttp
import aiohttp.client_exceptions
from yarl import URL
from celery import current_app
from typing import Dict

import logging

from ..tools.client_headers import headers
from ..tools.async_decorator import asyncio_decorator
from .. import config

logger = logging.getLogger("scrapper")


async def pull_nba_scoreboard(date: datetime.date):
    async with aiohttp.ClientSession(headers=headers) as session:
        url = f'https://www.espn.com/nba/scoreboard/_/date/{date.strftime("%G%m%d")}'
        try:
            async with session.get(url) as resp:
                if resp.status != 200:
                    message = "www.espn.com returns unexpected status code."
                    logger.error(message)
                    raise Exception(message)
                return await resp.text()
        except aiohttp.client_exceptions.ClientConnectorError as e:
            logger.error(e)
            raise e


def parse_scoreboard(html_string: str) -> Dict:
    pattern = re.compile(r'<script>window.espn.scoreboardData\s+=\s+(\{.*?\});')
    matched = pattern.findall(html_string)
    if matched:
        return json.loads(matched[0])
    raise Exception("Could not find scoreboard data.")


def convert_games(game: Dict):
    return game


def extract_games(scoreboard: Dict) -> list:
    return list(map(convert_games, scoreboard["events"]))


@current_app.task(name="scrap_nba_task")
@asyncio_decorator
async def scrap_nba_task():
    # uncomment this and comment the 57 line for testing
    # html_scoreboard = await pull_nba_scoreboard(datetime.date(year=2019, month=11, day=10))
    html_scoreboard = await pull_nba_scoreboard(datetime.date.today())
    json_scoreboard = parse_scoreboard(html_scoreboard)
    games = extract_games(json_scoreboard)
    async with aiohttp.ClientSession(headers={"api_key": config.API_KEY}) as session:
        url_pattern = URL(config.API_URL) / "games"

        tasks = []
        for game in games:
            url = url_pattern / game["id"]
            tasks.append(session.put(url, json=game))

        await asyncio.gather(*tasks)

    print("Done")
