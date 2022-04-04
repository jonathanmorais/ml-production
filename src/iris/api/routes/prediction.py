from fastapi import APIRouter, Depends
from starlette.requests import Request
from iris.services.prediction import ClassIris
from iris.core  import security

router = APIRouter()
class_iris = ClassIris.classify_iris

@router.post('/predict')
def predict(features: dict) -> dict:
    authenticated: bool = Depends(security.validate_request)
    return class_iris(features)