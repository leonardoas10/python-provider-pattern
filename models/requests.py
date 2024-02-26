from pydantic import BaseModel

class RequestJsonPlaceHolderUpdate(BaseModel):
    id: int
    title: str