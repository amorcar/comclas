from typing import Callable
from fastapi import FastAPI
import logging

def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app()  -> None:
        logging.info("Creating FASTAPi app")
    return start_app

def create_stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        logging.info("Stopping FASTAPi app")

    return stop_app
