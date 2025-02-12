from fastapi import APIRouter, HTTPException  #type: ignore
from utils.db_conection import get_db_client #type: ignore
from pydantic import BaseModel

client = get_db_client()
db = client["fastapi"]
class Todo(BaseModel):
    title: str
    description: str
    status: str
    
    
    


write_router = APIRouter()
@write_router.post("/todo")
def create_todo(todo: Todo):
    try :
         
        
        db.todo.insert_one({
            "title": todo.title,
            "description": todo.description,
            "status": todo.status
            })
             
        return {
           "data": { },
            "error": None,
            "message": "Todo created successfully",
            "status": "success"
            }
        
        
    except Exception as e:
        return {
            "data": [],
            "error": "Error creating todo",
            "message": str(e),
            "status": "failed"
            }
        
        
 