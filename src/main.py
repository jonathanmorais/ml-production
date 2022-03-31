import uvicorn
from fastapi import FastAPI
from fastapi import APIRouter
from iris import classify_iris

app = FastAPI()
router = APIRouter()

@app.post('/predict')
class Prediction:
    def __init__(self, iris_features) -> None:
        pass

    def predict(iris_features: dict):
        return classify_iris(iris_features)

@app.get('/health', status_code=200)
class Health:
    async def health_check():
        return 'Iris classifier is all ready!'

app.include_router(router, prefix='/iris')


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, log_level="debug")
