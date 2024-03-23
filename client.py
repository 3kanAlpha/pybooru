import requests, os, json
from requests.auth import HTTPBasicAuth
import settings

class DanbooruClient:
    def __init__(self, username, api_key):
        self.username = username
        self.api_key = api_key

    def get_post(self, post_id: int):
        """Fetch a post from Danbooru by its ID."""
        print(f"Fetching post #{post_id}...")
        url = f"https://danbooru.donmai.us/posts/{post_id}.json"
        headers = {
            "Content-Type": "application/json",
        }
        response = requests.get(
            url, headers=headers, auth=HTTPBasicAuth(self.username, self.api_key)
        )
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def search_posts(self, tags: str, limit: int = 200):
        """Fetch posts from Danbooru by tags."""
        print(f"Fetching posts with tags: {tags}...")
        url = "https://danbooru.donmai.us/posts.json"
        headers = {
            "Content-Type": "application/json",
        }
        params = {
            "tags": tags,
            "limit": limit,
        }
        response = requests.get(
            url,
            headers=headers,
            params=params,
            auth=HTTPBasicAuth(self.username, self.api_key),
        )
        if response.status_code == 200:
            return response.json()
        else:
            return None

# 以下サンプルコード
def main():
    client = DanbooruClient(settings.USERNAME, settings.API_KEY)
    posts = client.search_posts(tags="shirakami_fubuki")

    with open("posts.json", "w") as f:
        json.dump(posts, f, indent=2)

if __name__ == "__main__":
    main()
