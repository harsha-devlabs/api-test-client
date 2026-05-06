import requests


class PostsClient:

    URL = "https://jsonplaceholder.typicode.com/posts"

    def get_all_posts(self):
        return requests.get(self.URL)

    def get_post(self, post_id):
        return requests.get(f"{self.URL}/{post_id}")

    def create_post(self, payload):
        return requests.post(self.URL, json=payload)

    def update_post(self, post_id, payload):
        return requests.put(f"{self.URL}/{post_id}", json=payload)

    def delete_post(self, post_id):
        return requests.delete(f"{self.URL}/{post_id}")