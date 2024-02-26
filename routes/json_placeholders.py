from fastapi import APIRouter, Depends
from services.json_placeholders import JsonPlaceHolderService
from typing import List
from models.json_placeholders import JsonPlaceHolder

router = APIRouter()

@router.get("/", response_model=List[JsonPlaceHolder])
def get_users(service: JsonPlaceHolderService = Depends(JsonPlaceHolderService)):
    users = service.get_json_placeholders()
    
    return users
    # users, status, error = service.get_json_placeholders()

    # if error:
    #     return {"error": error}, status

    # return users, status
