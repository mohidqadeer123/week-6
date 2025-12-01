import requests
import pandas as pd


# Exercise 1
class Genius:

    def __init__(self, access_token):
        if not access_token:
            raise ValueError("Access token is required")
        self.access_token = access_token

        self.base_url = "https://api.genius.com"
        self.headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

# Exercise 2
   
    def get_artist(self, search_term):
        """
        Search Genius and return artist info for the first hit.
        """
        search_url = f"{self.base_url}/search"
        params = {"q": search_term}

        resp = requests.get(search_url, headers=self.headers, params=params)
        json_data = resp.json()

        hits = json_data['response']['hits']

        if not hits:
            return {}

        # First hit primary artist ID
        artist_id = hits[0]["result"]["primary_artist"]["id"]

        # Artist API
        artist_url = f"{self.base_url}/artists/{artist_id}"
        artist_resp = requests.get(artist_url, headers=self.headers)
        artist_data = artist_resp.json()['response']['artist']

        return artist_data

    
# Exercise 3

    def get_artists(self, search_terms):

        rows = []

        for term in search_terms:
            artist = self.get_artist(term)

            rows.append({
                "search_term": term,
                "artist_name": artist.get("name"),
                "artist_id": artist.get("id"),
                "followers_count": artist.get("followers_count")
            })

        return pd.DataFrame(rows)
