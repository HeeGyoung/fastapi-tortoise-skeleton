from http import HTTPStatus

from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from tortoise.exceptions import DoesNotExist


async def does_not_exist_handler(request: Request, e: DoesNotExist):
    return JSONResponse(status_code=HTTPStatus.NOT_FOUND, content={"message": str(e)})


async def pydantic_validation_error_handler(request: Request, e: ValidationError):
    return JSONResponse(
        status_code=HTTPStatus.BAD_REQUEST, content={"message": e.errors()}
    )
