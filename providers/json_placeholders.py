from typing import List
from models.json_placeholders import JsonPlaceHolder

class JsonPlaceHolderProvider:
    def __init__(self) -> None:
        self.url = "https://jsonplaceholder.typicode.com/todos"
    
    def get_users(self) -> List[JsonPlaceHolder]:
        return [JsonPlaceHolder(userId="1", id="1", title="1", completed=False)]

    
    # def get_users(self) -> Tuple[List[JsonPlaceHolder], int, str]:
    #     return [JsonPlaceHolder(userId="1", id="1", title="1", completed=False)], 200, None

        # response = requests.get(self.url)

        # if response.status_code != 200:
        #     return [], response.status_code, response.reason

        # json_placeholders = response.json()

        # return [JsonPlaceHolder(
        #     userId=str(json_placeholder['userId']),
        #     id=str(json_placeholder['id']),
        #     title=json_placeholder['title'],
        #     completed=json_placeholder['completed']
        # ) for json_placeholder in json_placeholders], response.status_code, None