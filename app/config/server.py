from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

from app.config.routes import __router__
from app.internal.events.startup import on_startup, on_loop_startup


class Server:

    __app: FastAPI

    def __init__(self, app: FastAPI) -> None:

        self.__app = app
        self.__register_routes(app)
        self.__register_events(app)

    def get_app(self) -> FastAPI:

        return self.__app

    @staticmethod
    def __register_events(app: FastAPI) -> None:

        app.on_event("startup")(repeat_every(seconds=60*60*12)(on_startup))
        app.on_event("startup")(repeat_every(seconds=5)(on_loop_startup))

    @staticmethod
    def __register_routes(app: FastAPI) -> None:

        __router__.register_routes(app)
