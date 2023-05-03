from fastapi import FastAPI, Security
from fastapi_pagination import add_pagination
from pydantic import ValidationError
from tortoise.contrib.fastapi import register_tortoise
from tortoise.exceptions import DoesNotExist

from config.settings import TORTOISE_ORM, settings
from routers import event, login, order, user
from services.exceptions.handler import (
    does_not_exist_handler,
    pydantic_validation_error_handler,
)

app = FastAPI(title=settings.APP_NAME)
register_tortoise(
    app,
    config=TORTOISE_ORM,
)
app.include_router(login.router)
app.include_router(user.router)
app.include_router(event.router)
app.include_router(order.router)
app.add_exception_handler(DoesNotExist, does_not_exist_handler)
app.add_exception_handler(ValidationError, pydantic_validation_error_handler)
add_pagination(app)
