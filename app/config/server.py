from fastapi import FastAPI
from app.config.routes import __router__


class Server:

    __app: FastAPI

    def __init__(self, app: FastAPI) -> None:

        self.__app = app
        self.__register_routes(app)

    def get_app(self) -> FastAPI:

        return self.__app

    @staticmethod
    def __register_event(app):

        ...

    @staticmethod
    def __register_routes(app):

        __router__.register_routes(app)
