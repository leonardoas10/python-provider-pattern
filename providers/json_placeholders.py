import httpx
import asyncio
from typing import List, Tuple
from models.json_placeholders import JsonPlaceHolder
from models.requests import RequestJsonPlaceHolderUpdate

class JsonPlaceHolderProvider:
    async def get_json_placeholders(self) -> Tuple[List[JsonPlaceHolder], int, str]:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://jsonplaceholder.typicode.com/todos")
            if response.status_code != 200:
                return [], response.status_code, response.reason
            
            return [JsonPlaceHolder(**item) for item in response.json()], response.status_code, None
    
    async def get_json_placeholder(self, id: str) -> Tuple[JsonPlaceHolder, int, str]:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://jsonplaceholder.typicode.com/todos/{}".format(id))
            if response.status_code != 200:
                return [], response.status_code, response.reason
            
            return response.json(), response.status_code, None
    
    async def update_place_holder(self, body: RequestJsonPlaceHolderUpdate) -> Tuple[JsonPlaceHolder, int, str]:
        user, status, err = await self.get_json_placeholder(body["id"])
        user["title"] = body["title"]
        
        return user, status, err
    
    async def change_title(self, user: JsonPlaceHolder, title: str) -> JsonPlaceHolder:
        return JsonPlaceHolder(
            id=user.id,
            userId=user.userId,
            title=title,
            completed=user.completed
        )
    
    async def concurrent_change_titles(self) -> Tuple[List[JsonPlaceHolder], int, str]:
        users, status, err = await self.get_json_placeholders()
        if err:
            return None, status, err

        # Create a list of coroutines to change titles concurrently
        coroutines = [self.change_title(user, f"Titulo {user.id}") for user in users]
        
        # Run coroutines concurrently
        results = await asyncio.gather(*coroutines, return_exceptions=True)
    
        # Check for errors in results
        for result in results:
            if isinstance(result, Exception):
                return None, 500, str(result)
        
        return results, status, err