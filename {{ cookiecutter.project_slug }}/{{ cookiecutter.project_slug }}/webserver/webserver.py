from typing import List

from fastapi import Depends, FastAPI, HTTPException

from starlette.requests import Request
from starlette.responses import Response

from {{ cookiecutter.project_slug }}.logging import log_group, Logger
from {{ cookiecutter.project_slug }} import schemas

log = Logger(' {{ cookiecutter.project_slug }}.webserver')
log_group.add_logger(log)

app = FastAPI(title="{{ cookiecutter.project_name }}",
              description="{{ cookiecutter.description }}",
              version="{{ cookiecutter.version }}")

@app.middleware("http")
async def log_request_and_response_status(request: Request, call_next):
    """Log every request"""
    response = await call_next(request)
    log.info("{} {} {}".format(request.method, request.url, response.status_code))
    return response

@app.get("/ping", response_model=schemas.Message)
async def health_check():
    """Return a 200 to indicate that the webserver is working"""
    return schemas.Message(detail='pong')



