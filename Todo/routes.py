from fastapi import APIRouter, HTTPException
import models

router = APIRouter()

@router.get("/todos")
def todo():
    return models.todos

@router.post("/todo")
def add_todo(item: models.CreateItem):
    models.counter += 1
    models.todos.append({"id": models.counter - 1, "task": item.task, "completed": False})
    return {"id": models.counter - 1, "task": item.task, "completed": False}

@router.put("/todo/{id}")
def update_todo(id: int, item: models.UpdateItem):
    for todo in models.todos:
        if todo["id"] == id:
            if item.task is not None:
                todo["task"] = item.task
            todo["completed"] = item.completed
            return models.todos
    raise HTTPException(status_code=404, detail="No Task found!")

@router.delete("/todo/{todo_id}")
def delete_todo(todo_id: int):
    for i, todo in enumerate(models.todos):
        if todo["id"] == todo_id:
            if todo["completed"] == True:
                deleted = models.todos.pop(i)
                return {"message": "Task Completed!", "task": deleted}
            raise HTTPException(status_code=400, detail="Task not yet completed")
    raise HTTPException(status_code=404, detail="No Task found!")