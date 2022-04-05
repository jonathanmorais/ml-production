from matplotlib.pyplot import title
import uvicorn
from fastapi import FastAPI
from fastapi import APIRouter
from iris.core.config import (API_PREFIX, APP_NAME, APP_VERSION, API_METRICS, IS_DEBUG)
from iris.api.routes.router import api_router
from starlette_prometheus import metrics, PrometheusMiddleware

app = FastAPI()
router = APIRouter()

app.include_router(router, prefix=API_PREFIX)

def get_app() -> FastAPI:
    fast_app = FastAPI(title=APP_NAME, version=APP_VERSION)
    fast_app.include_router(api_router, prefix=API_PREFIX)
    fast_app.add_middleware(PrometheusMiddleware)
    fast_app.add_route(API_METRICS, metrics)
    return fast_app

app = get_app()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080, log_level="debug")
