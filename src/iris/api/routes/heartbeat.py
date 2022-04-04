from fastapi import APIRouter

router = APIRouter()

@router.get("/heartbeat", name="health", status_code=200)
async def health_check():
    return 'Iris classifier is all ready!'  