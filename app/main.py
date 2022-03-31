import uvicorn
from fastapi import FastAPI
from fastapi import APIRouter
from pkg.iris import classify_iris

app = FastAPI()
router = APIRouter()

@router.post('/predict')
def predict(iris_features: dict):
    return classify_iris(iris_features)

@app.get('/health', status_code=200)
async def health_check():
    return 'Iris classifier is all ready!'


app.include_router(router, prefix='/iris')


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8080, log_level="debug")
