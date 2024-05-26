from .controllers.product_controller import router as product_router
from .controllers.user_controller import router as user_router


def include_routes(app):
    app.include_router(product_router, prefix="/products", tags=["products"])
    app.include_router(user_router, prefix="/users", tags=["users"])
    return app

