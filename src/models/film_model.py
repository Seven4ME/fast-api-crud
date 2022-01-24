from pydantic import BaseModel


class FilmBase(BaseModel):
    name: str
    rating: float


class FilmIn(FilmBase):
    pass


class FilmOut(FilmBase):
    pass
