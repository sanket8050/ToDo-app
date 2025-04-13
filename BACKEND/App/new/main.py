from fastapi import FastAPI
from sqlmodel import SQLModel,Field



#creare Model 
class Todo(SQLModel):

    


app = FastAPI()

@app.get('/')
async def root():
    return {"message": "welcome todo Worldfckhdbn "}

@app.get('/todo/')
async def read_todo():
    return {"todo": "This is a todo"}
 