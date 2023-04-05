from dataclasses import dataclass
from fastapi import FastAPI


@dataclass(frozen=True)
class Router:

    routes: tuple

    def register_routes(self, app: FastAPI):

        for route in self.routes:
            app.include_router(route)
