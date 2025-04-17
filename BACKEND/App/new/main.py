from fastapi import FastAPI
from sqlmodel import SQLModel,Field,create_engine,Session

import settings




# Adjust the import to work without modifying the Python path

#creare Model (two types)
    #data model
    #table model




class Todo(SQLModel,table=True):
    id : int | None = Field(default=None,primary_key=True)
    content : str = Field(index=True ,min_length = 3 ,max_length = 54)
    is_completed : bool = Field(default=False)

    
connection_string : str = str(settings.Database_url).replace("postgresql" , "postgresql + psycopg")

engine = create_engine(connection_string , connect_args={"sslmode" : "require"},pool_recycle=300,pool_size=10, max_overflow=20 , echo=True)

todo1 : Todo = Todo(content="first task")
todo2 : Todo = Todo(content="second task")

# session :saperate session for each transaction

session = Session(engine)

# add todos in database
session.add(todo1)
session.add(todo2)
print(f'before commint {todo1}')
session.commit()
print(f'after commint {todo1}')
session.close()


SQLModel.metadata.create_all(engine)
app = FastAPI()
@app.get('/')
async def root():
    return {"message": "welcome todo Worldfckhdbn "}

@app.get('/todo/')
async def read_todo():
    return {"todo": "This is a todo"}
 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
