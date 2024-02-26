from pydantic import BaseModel

class JsonPlaceHolder(BaseModel):
    userId: str
    id: str
    title: str
    completed: bool
