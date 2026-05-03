from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def greet():
    return {"message" : "Hello Jeff"}

class Item(BaseModel):
    name: str
    price: float
    
expenses = []

@app.post("/expenses")
def create_expense(item: Item):
    length = len(expenses)
    expenses.append({ "id" : length, "name" : item.name, "price" : item.price})
    return {"id" : length, "name" : item.name, "price": item.price}

@app.get("/expenses")
def get_expense():
    return expenses

@app.put("/expenses/{id}")
def update_expenses(id: int, item: Item):
    for expense in expenses:
        if expense["id"] == id:
            expense["name"] = item.name
            expense["price"] = item.price
            return expense
            
@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    for i, expense in enumerate(expenses):
        if expense["id"] == expense_id:
            deleted = expenses.pop(i)
            return {"message": "Expense deleted", "expense": deleted}
    raise HTTPException(status_code=404, detail="Expense not found")