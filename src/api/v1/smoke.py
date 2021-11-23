import http
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class OK(BaseModel):
    message: str
    status: str

@router.get("/smoke/", description="Health check of app", response_model=OK)
async def smoke_resource():
    return {"message": "OK", "status": http.HTTPStatus.OK}