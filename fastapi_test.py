from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/")
def root() -> dict[str, str]:
    return {"Hello": "world"}


@app.get("/items/{id}")
def item(id: int, q: Union[str, None] = None) -> dict[str, Union[int, str, None]]:
    return {"id": id, "q": q}
