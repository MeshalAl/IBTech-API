import os, sys
from uvicorn import run
from fastapi import FastAPI
from core.error_handlers import register_error_handlers



from _config.config import load_env
load_env('../.env')

from api.routes import include_routes
app = include_routes(FastAPI())
register_error_handlers(app)

if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=8000)
