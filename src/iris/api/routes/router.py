from fastapi import APIRouter
from iris.api.routes import heartbeat, prediction, metrics
from fastapi import FastAPI

api_router = APIRouter()
api_router.include_router(heartbeat.router, tags=["health"], prefix="/health")
api_router.include_router(prediction.router, tags=["classification"], prefix="/classification")