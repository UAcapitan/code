
import fastapi

from typing import Optional
from starlette.requests import Request
from starlette.templating import Jinja2Templates


router = fastapi.APIRouter()
templates = Jinja2Templates("templates")

token: Optional[str] = None

@router.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "home.html", 
        {
            "request": request,
            "token": token
        }
    )
