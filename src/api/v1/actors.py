from typing import List

from fastapi import APIRouter

from src.config.settings import get_settings
from src.controllers import StorageController
from src.models.actor_model import ActorOut

settings = get_settings()
router = APIRouter(prefix=settings.actors_prefix)


@router.get("/", description="get list of actors", response_model=List[ActorOut])
async def get_actors_list():
    response = await StorageController.search(index="actors")

    return [
        ActorOut(
            first_name=hit["_source"]["first_name"],
            second_name=hit["_source"]["second_name"],
        )
        for hit in response["hits"]["hits"]
    ]


@router.get("/{actor_id}", description="get actor by id")
async def get_actor_by_id(actor_id: str):
    response = await StorageController.get(index="actors", id=actor_id)

    return {
        "name": response["_source"]["first_name"],
        "rating": response["_source"]["second_name"],
    }
