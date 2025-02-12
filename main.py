from fastapi import FastAPI, HTTPException  #type: ignore
from routes.read_route import read_router
from fastapi.responses import JSONResponse  #type: ignore
from fastapi.exceptions import RequestValidationError  #type: ignore
from fastapi.requests import Request   #type: ignore
from routes.write_route import write_router  #type: ignore
from routes.delete_route import delete_router  #type: ignore
from routes.update_route import update_router  #type: ignore
app = FastAPI()


@app.get("/")   
def read_root():
    return {"status": "Server is running"}

app.include_router(write_router,tags=["Write"],prefix="/write")
app.include_router(read_router,tags=["Read"],prefix="/read")
app.include_router(delete_router,tags=["Delete"],prefix="/delete")
app.include_router(update_router,tags=["Update"],prefix="/update")
#for custom ecpections handling
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        errors.append({
            "field": ".".join(map(str, error["loc"])),  # Converts tuple path to a string
            "message": error["msg"]
        })
    
    return JSONResponse(
        status_code=400,
        content={
            "status": "error",
            "message": "Validation failed",
            "errors": errors
        }
    )

