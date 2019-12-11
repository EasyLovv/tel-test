from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent

install_requires = [
    "celery==4.3.0",
    "aiohttp==3.6.2"
]

dev_requires = []

setup(
    name="scrapper",
    version="0.1",
    packages=["scrapper"],
    install_requires=install_requires,
    author="Taras Protsenko",
    author_email="easylovv@gmail.com",
    maintainer="Taras Protsenko",
    maintainer_email="easylovv@gmail.com",
    description="The worker and heartbeat for scrapper.",
    include_package_data=True,
    extras_require={"dev": dev_requires},
    long_description=(here / "README.md").read_text("utf-8").strip(),
    long_description_content_type="text/markdown",
)
