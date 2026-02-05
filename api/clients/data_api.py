import requests 


class DataAPI:
    def create_item(self,cookies):
        payload = {
            "title":"Test Item", 
            "description":"created via API"

         }

         response = requests.post("https://example.com/api/items",
            json=payload,
            cookies=cookies
         )
         return response

    def delete_item(self,item_id,cookies):
        response = requests.delete(
            f"https://example.com/api/items/{item_id}",
            cookies=cookies
        )

        return response
