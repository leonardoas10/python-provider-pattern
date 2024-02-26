from typing import List
from fastapi import APIRouter, Depends, Request, Response, HTTPException, Path
from services.json_placeholders import JsonPlaceHolderService
from models.json_placeholders import JsonPlaceHolder
import json

router = APIRouter()

@router.get("/", response_model=List[JsonPlaceHolder])
async def get_users(response: Response, service: JsonPlaceHolderService = Depends(JsonPlaceHolderService)):
    users, status, error = await service.get_json_placeholders()
    
    if error:
        raise HTTPException(status_code=status, detail=error)

    response.status_code = status
    return users

@router.put("/", response_model=JsonPlaceHolder)
async def update_user(request: Request, response: Response, service: JsonPlaceHolderService = Depends(JsonPlaceHolderService)):
    body = await request.body()
    body_json = json.loads(body.decode("utf-8"))

    user, status, error = await service.update_place_holder(body = body_json)
    
    if error:
        raise HTTPException(status_code=status, detail=error)

    response.status_code = status
    return user

@router.get("/concurrent-change-titles", response_model=List[JsonPlaceHolder])
async def concurrent_change_titles(response: Response, service: JsonPlaceHolderService = Depends(JsonPlaceHolderService)):
    users, status, error = await service.concurrent_change_titles()
    
    if error:
        raise HTTPException(status_code=status, detail=error)

    response.status_code = status
    return users

@router.get("/{id}", response_model=JsonPlaceHolder)
async def get_user(response: Response, id: int = Path(..., title="The ID of the user to get"), service: JsonPlaceHolderService = Depends(JsonPlaceHolderService)):
    user, status, error = await service.get_json_placeholder(id)
    
    if error:
        raise HTTPException(status_code=status, detail=error)

    response.status_code = status
    return user