from typing import List

from fastapi import APIRouter

from src.config.settings import get_settings
from src.controllers import StorageController
from src.models.film_model import FilmOut

settings = get_settings()
router = APIRouter(prefix=settings.films_prefix)


@router.get("/", description="get list of films", response_model=List[FilmOut])
async def get_films_list():
    response = await StorageController.search(index="movies")
    return [
        FilmOut(name=hit["_source"]["title"], rating=hit["_source"]["rate"])
        for hit in response["hits"]["hits"]
    ]


@router.get("/{film_id}", description="get film by id", response_model=FilmOut)
async def get_film_by_id(film_id: str) -> dict:
    response = await StorageController.get(index="movies", id=film_id)
    return {
        "name": response["_source"]["title"],
        "rating": response["_source"]["rate"],
    }
