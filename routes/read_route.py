from fastapi import APIRouter #type: ignore
from utils.db_conection import get_db_client
from bson.objectid import ObjectId #type: ignore

read_router = APIRouter()
client = get_db_client()
db = client["fastapi"]

#read/todos
@read_router.get("/todo")
def read_todos():
    try:
        
        todos = db.todo.find()
        listTodos = []
        for todo in todos:
            listTodos.append({
                "Id": str(todo["_id"]),
                "Title": todo["title"],
                "Description": todo["description"],
                "Status": todo["status"]
                
             })
        return {
            "data": listTodos,
            "error": None,
            "message": "Todos read successfully",
            "status": "success"
            }
    except Exception as e:
         return {
            "data": [],
            "error": "Error reading todos",
            "message": str(e),
            "status": "failed"
            }

#read/todo/{id}
        
@read_router.get("/todobyid/{id}")
def read_todo_by_id(id: str):
    try:
        todo = db.todo.find_one({"_id": ObjectId(id)})
        return {
            "data": {
                "Id": str(todo["_id"]),
                "title": todo["title"],
                "Description": todo["description"],
                "Status": todo["status"]
                
                },
            
            "error": None,
            "message": "Todo read successfully",
            "status": "success"
            }
    except Exception as e:
         return {
            "data": {},
            "error": "Error reading todo",
            "message": str(e),
            "status": "failed"
            }
         
@read_router.get("/todobytitle/{title}")
def read_todo_by_title(title: str):
    try:
        todo = db.todo.find_one({"title": title})
        return {
            "data": {
                "Id": str(todo["_id"]),
                "title": todo["title"],
                "Description": todo["description"],
                "Status": todo["status"]
                
                },
            
            "error": None,
            "message": "Todo read successfully",
            "status": "success"
            }
        
    except Exception as e:
        return{
            
            "data": None,
            "error": "Error reading todo",
            "message": str(e),
            "status": "failed"
        }