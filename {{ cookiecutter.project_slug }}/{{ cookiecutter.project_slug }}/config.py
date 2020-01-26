import os
import configparser
import logbook

{{ cookiecutter.project_slug|upper }}_HOME = os.getenv('{{ cookiecutter.project_slug|upper }}_HOME', os.path.dirname(__file__))
CONFIG_PATH = os.getenv('{{ cookiecutter.project_slug|upper }}_CONFIG_PATH', os.path.join({{ cookiecutter.project_slug|upper }}_HOME, '{{ cookiecutter.project_name}}.ini'))
_parser = configparser.ConfigParser()
_parser.read(CONFIG_PATH)

LOG_FILE = os.getenv('{{ cookiecutter.project_slug|upper }}_LOG_FILE', _parser['{{ cookiecutter.project_slug }}'].get('log_file'))
LOG_LEVEL = os.getenv('{{ cookiecutter.project_slug|upper }}_LOG_LEVEL', _parser['{{ cookiecutter.project_slug }}'].get('log_level'))

if LOG_LEVEL.lower() == "critical":
    LOG_LEVEL = logbook.CRITICAL
elif LOG_LEVEL.lower() == "error":
    LOG_LEVEL = logbook.ERROR
elif LOG_LEVEL.lower() == "warning":
    LOG_LEVEL = logbook.WARNING
elif LOG_LEVEL.lower() == "info":
    LOG_LEVEL = logbook.INFO
elif LOG_LEVEL.lower() == "debug":
    LOG_LEVEL = logbook.DEBUG
else:
    LOG_LEVEL = logbook.NOTSET
try:
    PORT = int(os.getenv('{{ cookiecutter.project_slug|upper }}_RUN_PORT', _parser['webserver'].get('port')))
except ValueError:
    raise ValueError("Port option must be an integer")
    
DB_URI = os.getenv('{{ cookiecutter.project_slug|upper }}_DB_URI', _parser['{{ cookiecutter.project_slug }}'].get('db_uri'))
