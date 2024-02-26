import httpx
from typing import List, Tuple
from models.json_placeholders import JsonPlaceHolder

class JsonPlaceHolderProvider:
    async def get_json_placeholders(self) -> Tuple[List[JsonPlaceHolder], int, str]:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://jsonplaceholder.typicode.com/todos")
            if response.status_code != 200:
                return [], response.status_code, response.reason
            
            return [JsonPlaceHolder(**item) for item in response.json()], response.status_code, None