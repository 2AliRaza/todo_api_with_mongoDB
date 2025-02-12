from fastapi import APIRouter, HTTPException  #type: ignore
from utils.db_conection import get_db_client #type: ignore
client=get_db_client()
db=client["fastapi"]
delete_router = APIRouter()
@delete_router.delete("/todo")
def delete_todo(title: str):
    try:
        db.todo.delete_one({"title": title})      
        return {
            "data": { },
            "error": None,
            "message": "Todo deleted successfully",
            "status": "success"
            }
    except Exception as e:
        return {
            "data": [],
            "error": "Error deleting todo",
            "message": str(e),
            "status": "failed"
            }
        
@delete_router.delete("/todo/all")
def delete_all_todo():
    try:
        db.todo.delete_many({})      
        return {
            "data": { },
            "error": None,
            "message": "All Todos deleted successfully",
            "status": "success"
            }
    except Exception as e:
        return {
            "data": [],
            "error": "Error deleting all todos",
            "message": str(e),
            "status": "failed"
            }