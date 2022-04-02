import uvicorn
from fastapi import FastAPI
from fastapi import APIRouter
from services.prediction import ClassIris

app = FastAPI()
router = APIRouter()
class_iris = ClassIris.classify_iris

@app.post('/predict')
def predict(features: dict) -> dict:
    return class_iris(features)

@app.get('/health', status_code=200)
async def health_check():
    return 'Iris classifier is all ready!'    

app.include_router(router, prefix='/iris')


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, log_level="debug")
