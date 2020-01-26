import os
import click
from logbook import StderrHandler, TimedRotatingFileHandler
from {{ cookiecutter.project_slug }}.logging import log_group, Logger
from {{ cookiecutter.project_slug }} import config

log = Logger('{{ cookiecutter.project_slug }}.cli')
log_group.add_logger(log)

@click.group()
@click.option("--log-file")
@click.option("--log-level")
def cli(log_file, log_level):
    """
    {{ cookiecutter.description }}
    """
    if log_file:
        config.LOG_FILE = log_file
    if log_level:
        config.LOG_LEVEL = log_level
    if config.LOG_FILE:
        handler = TimedRotatingFileHandler(log_file,
                                 date_format='%Y-%m-%d')
    else:
        handler = StderrHandler()
    handler.push_application()

@cli.command()
@click.option("--port", type=int, help="The port to run on")
@click.option("--reload", is_flag=True, default=False)
def run(port, reload):
    """Run the {{ cookiecutter.project_name }} webserver"""
    import uvicorn
    from {{ cookiecutter.project_slug }} import webserver, config
    if port:
        config.PORT = port
    log.info("Starting webserver...")
    uvicorn.run(
        webserver.app,
        host='0.0.0.0',
        port=config.PORT,
        log_level=config.LOG_LEVEL,
        reload=reload)

@cli.command()
def upgradedb():
    """Upgrade the db"""
    from alembic import command
    from alembic.config import Config
    log.info("Applying migrations...")    
    alembic_config = Config(config.CONFIG_PATH)
    alembic_config.set_main_option('script_location', os.path.join(config.{{ cookiecutter.project_slug|upper }}_HOME, 'migrations'))
    alembic_config.set_main_option('sqlalchemy.url', config.DB_URI)
    command.upgrade(alembic_config, 'head')
