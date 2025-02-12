from fastapi import APIRouter, HTTPException  #type: ignore
from utils.db_conection import get_db_client #type: ignore
from pydantic import BaseModel  #type: ignore
from bson.objectid import ObjectId #type: ignore

class Todo(BaseModel):
    title: str
    description: str
    status: str
client=get_db_client()
db=client["fastapi"]
update_router = APIRouter()
@update_router.put("/todobyname/{title}")
def update_todo_by_name(title: str,todo: Todo):
    try:
        if db.todo.find_one({"title": title}) is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        db.todo.update_one({ "title": title}, 
        {"$set":
            {"title": todo.title,
             "description": todo.description,
             "status": todo.status
             }})
        
        return {
            "data": { },
            "error": None,
            "message": "Todo updated successfully",
            "status": "success"
            }
    except Exception as e:
        return {
            "data": None,
            "error": str(e),
            "message": "Todo not updated",
            "status": "error"
            }
@update_router.put("/todobyid/{id}")
def update_todo_by_id(id:str,todo: Todo):
    try:
        if db.todo.find_one({"_id": ObjectId(id)}) is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        db.todo.update_one({ "_id": ObjectId(id) }, 
        {"$set":
            {"title": todo.title,
             "description": todo.description,
             "status": todo.status
             }})
        
        return {
            "data": {} ,
            "error": None,
            "message": "Todo updated successfully",
            "status": "success"
            }
    except Exception as e:
        return {
            "data": None,
            "error": str(e),
            "message": "Todo not updated",
            "status": "error"
            }