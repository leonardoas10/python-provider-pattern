from providers.json_placeholders import JsonPlaceHolderProvider 
from models.json_placeholders import JsonPlaceHolder
from typing import List, Tuple

class JsonPlaceHolderService:
    def __init__(self, json_placeholders_provider: JsonPlaceHolderProvider) -> None:
        self.json_placeholders_provider = json_placeholders_provider
    
    def get_json_placeholders(self) -> List[JsonPlaceHolder]:
        return [JsonPlaceHolder(userId="1", id="1", title="1", completed=False)]
        # users, status, err = self.json_placeholders_provider.get_users()
        
        # if err:
        #     print(f"Error get_json_placeHolders {err}")
        #     return users, status, f"error: {err}"

        # return users, status, None