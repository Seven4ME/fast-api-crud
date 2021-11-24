import http

from fastapi import APIRouter

router = APIRouter()


@router.get("/smoke/", description="Health check of app")
async def smoke_resource():
    return {"message": "OK", "status": http.HTTPStatus.OK}
