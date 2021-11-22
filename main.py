from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/smoke/")
def read_async_recource():
    return {"message": "Ok"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}