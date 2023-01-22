from fastapi import FastAPI
from typing import Optional

from pydantic import BaseModel

from fastapi.responses import RedirectResponse

app = FastAPI()

inventory = {
    1: {"name": "Foo", "price": 50, "brand": "Bar"},
    2: {"name": "Baz", "price": 30, "brand": "Qux"},
}


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

# change read_root displayname


@app.get("/", tags=["Root"], summary="Redirect to /docs")
async def index():
    return RedirectResponse(url="/docs")


@app.get("/items")
async def get_item(item_id: Optional[int] = None):
    if item_id is None:
        return inventory
    if item_id not in inventory:
        return {"Error": "Item ID not found!"}
    return inventory[item_id]


@app.post("/add_item/")
async def add_item(item: Item):
    item_id = len(inventory) + 1
    inventory[item_id] = {"name": item.name, "price": item.price, "brand": item.brand}
    return inventory[item_id]


@app.put("/update_item/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id not in inventory:
        return {"Error": "Item ID not found!"}
    inventory[item_id] = {"name": item.name, "price": item.price, "brand": item.brand}
    return inventory[item_id]


@app.delete("/delete_item/{item_id}")
async def delete_item(item_id: int):
    if item_id not in inventory:
        return {"Error": "Item ID not found!"}
    del inventory[item_id]
    return {"Success": "Item deleted!"}


@app.delete("/delete_all_items")
async def delete_all_items():
    inventory.clear()
    return {"Success": "All items deleted!"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
