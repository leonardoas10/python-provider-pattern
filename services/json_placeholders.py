from typing import List, Tuple
from fastapi import Depends
from models.json_placeholders import JsonPlaceHolder, RequestJsonPlaceHolderUpdate
from providers.json_placeholders import JsonPlaceHolderProvider

class JsonPlaceHolderService:
    def __init__(self, provider: JsonPlaceHolderProvider = Depends(JsonPlaceHolderProvider)):
        self.provider = provider

    async def get_json_placeholders(self) -> Tuple[List[JsonPlaceHolder], int, str]:
        users, status, err = await self.provider.get_json_placeholders()
        return users, status, err

    async def get_json_placeholder(self, id: str) -> Tuple[JsonPlaceHolder, int, str]:
        user, status, err = await self.provider.get_json_placeholder(id)
        return user, status, err
    
    async def update_place_holder(self, body: RequestJsonPlaceHolderUpdate) -> Tuple[JsonPlaceHolder, int, str]:
        user, status, err = await self.provider.update_place_holder(body)
        return user, status, err
    
    async def concurrent_change_titles(self) -> Tuple[JsonPlaceHolder, int, str]:
        user, status, err = await self.provider.concurrent_change_titles()
        return user, status, err