from app.config.routes.routes import Router
from app.internal.routes import user, currency


__router__ = Router(routes=(user.router, currency.router,))
