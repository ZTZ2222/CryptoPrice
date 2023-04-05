from app.config.routes.routes import Router
from app.internal.routes import user


__router__ = Router(routes=(user.router,))
