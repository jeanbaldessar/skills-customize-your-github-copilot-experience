from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI(title="My REST API", description="A simple CRUD API", version="1.0.0")

# Pydantic model for data validation
class Item(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# In-memory database (replace with a real database in production)
items_db: List[Item] = [
    Item(id=1, title="Learn FastAPI", description="Study FastAPI basics", completed=False),
    Item(id=2, title="Build an API", description="Create a REST API", completed=False),
]

# TODO: Implement GET /items endpoint to retrieve all items

# TODO: Implement GET /items/{item_id} endpoint to retrieve a specific item

# TODO: Implement POST /items endpoint to create a new item

# TODO: Implement PUT /items/{item_id} endpoint to update an item

# TODO: Implement DELETE /items/{item_id} endpoint to delete an item

# Welcome endpoint (example)
@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI REST API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
