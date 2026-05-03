from pydantic import BaseModel
from typing import Optional
    
class CreateItem(BaseModel):
    task: str

class UpdateItem(BaseModel):
    task: Optional[str] = None
    completed: bool = False
    
todos = []
counter = 1