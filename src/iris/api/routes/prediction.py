from fastapi import APIRouter, Depends
from starlette.requests import Request
from iris.services.prediction import ClassIris

router = APIRouter()
class_iris = ClassIris.classify_iris

@router.post('/predict')
def predict(features: dict) -> dict:
    return class_iris(features)