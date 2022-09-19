from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "BBIYAK TEST"

@app.get("/cars")
def get_cars():
    return_msg = {
        f"id_{id}":id for id in range(10)
    }
    return return_msg

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
