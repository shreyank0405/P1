# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# # Data model
# class Item(BaseModel):
#     name: str
#     price: float

# # Sample data (FIXED)
# items = [
#     {"name": "Laptop", "price": 1000},
#     {"name": "Phone", "price": 500}
# ]

# # GET all items
# @app.get("/items/")
# def read_items():
#     return items

# # POST new item
# @app.post("/items/")
# def create_item(item: Item):
#     items.append(item.dict())
#     return item

# # GET item by ID
# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     if item_id < len(items):
#         return items[item_id]
#     return {"error": "Item not found"}


from fastapi import FastAPI
app = FastAPI(title="Cyber Security API")
@app.get("/")
def health_check():
    return {"status": "Server is running"}
