from typing import List, Tuple
from fastapi import Depends
from models.json_placeholders import JsonPlaceHolder
from providers.json_placeholders import JsonPlaceHolderProvider

class JsonPlaceHolderService:
    def __init__(self, provider: JsonPlaceHolderProvider = Depends(JsonPlaceHolderProvider)):
        self.provider = provider

    async def get_json_placeholders(self) -> Tuple[List[JsonPlaceHolder], int, str]:
        users, status, err = await self.provider.get_json_placeholders()
        if err:
            print(f"Error get_json_placeHolders {err}")
            return users, status, err
        return users, status, None