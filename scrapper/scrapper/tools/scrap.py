#!/bin/env python3
import asyncio
import datetime
import re
import json

import aiohttp
import aiohttp.client_exceptions
from typing import Dict

import logging

from scrapper.scrapper.tools.client_headers import headers

logger = logging.getLogger("scrapper")


def parse_scoreboard(html_string: str) -> Dict:
    pattern = re.compile(r'<script>window.espn.scoreboardData\s+=\s+(\{.*?\});')
    matched = pattern.findall(html_string)
    if matched:
        return json.loads(matched[0])
    raise Exception("Could not find scoreboard data.")


async def scrap_nba(date: datetime.date):
    async with aiohttp.ClientSession(headers=headers) as session:
        url = f'https://www.espn.com/nba/scoreboard/_/date/{date.strftime("%G%m%d")}'
        print(url)
        try:
            async with session.get(url) as resp:
                if resp.status != 200:
                    message = "www.espn.com returns unexpected status code."
                    logger.error(message)
                    raise Exception(message)
                return parse_scoreboard(await resp.text())
        except aiohttp.client_exceptions.ClientConnectorError as e:
            logger.error(e)
            raise e


async def main():
    data = await scrap_nba(datetime.date(year=2019, month=11, day=10))
    print(data)


if __name__ == "__main__":
    asyncio.run(main())
