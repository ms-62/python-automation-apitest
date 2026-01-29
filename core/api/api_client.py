import requests

class SimpleApiClient:
    def __init__(self,base_url):
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json"}
        
    def get_post(self, post_id=None):
            payload = {"userId": post_id}
            return requests.get(f"{self.base_url}/posts/",params=payload, headers=self.headers)
        
    def create_post(self, payload):
        return requests.post(f"{self.base_url}/posts",json=payload,headers=self.headers)
    
    def patch_post(self, post_id,data):
            return requests.patch(f"{self.base_url}/posts/{post_id}",json=data, headers=self.headers)
        
    def put_post(self, post_id,data):
        return requests.put(f"{self.base_url}/posts/{post_id}",json=data, headers=self.headers)