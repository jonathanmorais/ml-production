import fastapi
from matplotlib.pyplot import title
import uvicorn
from fastapi import FastAPI
from fastapi import APIRouter
from iris.services.prediction import ClassIris
from iris.core.config import (API_PREFIX, APP_NAME, APP_VERSION, IS_DEBUG)
from iris.api.routes.router import api_router

app = FastAPI()
router = APIRouter()

app.include_router(router, prefix=API_PREFIX)

def get_app() -> FastAPI:
    fast_app = FastAPI(title=APP_NAME, version=APP_VERSION)
    fast_app.include_router(api_router, prefix=API_PREFIX)

    return fast_app

app = get_app()    

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080, log_level="debug")
