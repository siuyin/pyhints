from fastapi import FastAPI  # type: ignore


app = FastAPI()


@app.get("/")
def root() -> dict[str, str]:
    return {"Hello": "world"}


@app.get("/items/{id}")
def item(id: int, q: str | None = None) -> dict[str, int | str | None]:
    return {"id": id, "q": q}
