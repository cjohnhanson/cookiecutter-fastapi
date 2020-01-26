#!/bin/env python
from setuptools import setup, find_packages

setup(
    name='{{ cookiecutter.project_name }}',
    version='0.1.0',
    include_package_data=True,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.command }}={{ cookiecutter.project_slug }}:cli',
            ]
        },
    install_requires=[
        'click',
        'pyyaml',
        'psycopg2-binary',
        "logbook",
        "alembic",
        "uvicorn",
        "fastapi"
    ]
)
