from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
    
class CreateItem(BaseModel):
    task: str

class UpdateItem(BaseModel):
    task: Optional[str] = None
    completed: bool = False
    
todos = []
counter = 1

@app.get("/todos")
def todo():
    return todos

@app.post("/todo")
def add_todo(item: CreateItem):
    global counter
    todos.append({"id": counter, "task" : item.task, "completed" : False})
    counter += 1
    return {"id" : counter - 1, "task" : item.task, "completed" : False}

@app.put("/todo/{id}")
def update_todo(id: int, item: UpdateItem):
    for todo in todos:
        if todo["id"] == id:
            if item.task is not None:
                todo["task"] = item.task
            todo["completed"] = item.completed
            return todos
    raise HTTPException(status_code=404, detail ="No Task found!")

@app.delete("/todo/{todo_id}")
def delete_todo(todo_id : int):
    for i,todo in enumerate(todos):
        if todo["id"] == todo_id:
            if todo["completed"] == True:
                deleted = todos.pop(i)
                return {"message" : "Task Completed!", "task": deleted}
            raise HTTPException(status_code=400, detail ="Task not yet completed")
    raise HTTPException(status_code=404, detail ="No Task found!")