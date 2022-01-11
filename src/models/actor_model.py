from pydantic import BaseModel


class ActorBase(BaseModel):
    first_name: str
    second_name: str


class ActorOut(ActorBase):
    pass


class ActorIn(ActorBase):
    pass
