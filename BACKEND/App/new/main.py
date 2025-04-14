from fastapi import FastAPI
from sqlmodel import SQLModel,Field



#creare Model (two types)
    #data model
    #table model

class Todo(SQLModel,table=True):
    id : int | None = Field(default=None,primary_key=True)
    content : str = Field(index=True ,min_length = 3 ,max_length = 54)
    is_completed : bool = Field(default=False)

    


app = FastAPI()

@app.get('/')
async def root():
    return {"message": "welcome todo Worldfckhdbn "}

@app.get('/todo/')
async def read_todo():
    return {"todo": "This is a todo"}
 