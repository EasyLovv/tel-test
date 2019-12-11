"""The asyncio_decorator module."""
from functools import wraps
import asyncio


def asyncio_decorator(func):
    """This decorator created to easy run the async code inside the tasks."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        asyncio.run(func(*args, **kwargs))

    return wrapper
