
import fastapi
import uvicorn


router = fastapi.APIRouter()


@router.get("/api/motd")
def message():
    return {
        "message": "Hello world!",
    }
