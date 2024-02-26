from typing import List
from fastapi import APIRouter, Depends, Response, HTTPException
from services.json_placeholders import JsonPlaceHolderService
from models.json_placeholders import JsonPlaceHolder

router = APIRouter()

@router.get("/", response_model=List[JsonPlaceHolder])
async def get_users(response: Response, service: JsonPlaceHolderService = Depends(JsonPlaceHolderService)):
    users, status, error = await service.get_json_placeholders()
    
    if error:
        raise HTTPException(status_code=status, detail=error)

    response.status_code = status
    return users
