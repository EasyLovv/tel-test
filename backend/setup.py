from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent

install_requires = [
    "Flask==1.1.1",
    "Flask-RESTful==0.3.7",
    "Flask-PyMongo==2.3.0"
]

dev_requires = [
]

setup(
    name="backend",
    version="0.1",
    packages=["backend"],
    url="",
    install_requires=install_requires,
    author="Taras Protsenko",
    author_email="easylovv@gmail.com",
    maintainer="Taras Protsenko",
    maintainer_email="easylovv@gmail.com",
    description="The api backend.",
    entry_points={"console_scripts": ["backend_launch=backend.app:run"]},
    include_package_data=True,
    extras_require={"dev": dev_requires},
    long_description=(here / "README.md").read_text("utf-8").strip(),
    long_description_content_type="text/markdown",
)
