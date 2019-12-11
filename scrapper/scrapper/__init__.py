"""The main worker package.
The worker initialization located here."""
from . import config

from celery import Celery

app = Celery("scrapper", broker=config.BROKER_URI)

# discover and register a tasks
app.autodiscover_tasks(["scrapper", "scrapper.periodic"])

# the beat configuration. This is a tasks which would be executing periodically.
app.conf.beat_schedule = {
    "scrap_nba_task": {"task": "scrap_nba_task", "schedule": 10, "options": {"expires": 10}},
}
