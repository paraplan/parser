from fastapi import FastAPI, Request
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse

from src.endpoint import router

app = FastAPI()


@app.exception_handler(ResponseValidationError)
async def http_exception_handler(request: Request, exc: ResponseValidationError):
    return JSONResponse(exc.body, status_code=500)


app.include_router(router)
