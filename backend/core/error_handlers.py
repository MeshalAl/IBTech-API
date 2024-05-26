# app/error_handlers.py
from fastapi import Request, FastAPI
from pydantic import BaseModel


class HTTPError(BaseModel):
    error_code: str
    error_description: str
    error_message: str


def register_error_handlers(app: FastAPI):
    from fastapi import HTTPException
    from fastapi.exceptions import RequestValidationError
    from fastapi.responses import JSONResponse

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        error_response = HTTPError(
            error_code="HTTP_ERROR",
            error_description=f"HTTP error occurred: {exc.status_code}",
            error_message=exc.detail,
        )
        return JSONResponse(
            status_code=exc.status_code, content=error_response.model_dump()
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):
        error_response = HTTPError(
            error_code="VALIDATION_ERROR",
            error_description="Invalid data provided",
            error_message=str(exc),
        )
        return JSONResponse(status_code=400, content=error_response.model_dump())

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        error_response = HTTPError(
            error_code="INTERNAL_SERVER_ERROR",
            error_description="An unexpected error occurred",
            error_message=str(exc),
        )
        return JSONResponse(status_code=500, content=error_response.model_dump())
