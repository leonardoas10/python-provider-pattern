from pydantic import BaseModel
from typing import List, Optional

class JsonPlaceHolder(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool
    

