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
        base_url = "http://api.genius.com/search"
        
        # Send a GET request to search for the artist
        response = requests.get(
            base_url,
            params={"q": search_term},
            headers={"Authorization": f"Bearer {self.access_token}"}
        )
        
        # Raise an error for unsuccessful request
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data: {response.status_code} - {response.text}")
        
        # Parse the JSON response
        search_results = response.json()

        # Extract the artist ID from the first "hit"
        try:
            artist_id = search_results["response"]["hits"][0]["result"]["primary_artist"]["id"]
            artist_api_path = search_results["response"]["hits"][0]["result"]["primary_artist"]["api_path"]
        except (KeyError, IndexError):
            raise Exception("No artist found for the given search term.")

        # Use the artist API path to fetch detailed artist information
        artist_url = f"http://api.genius.com{artist_api_path}"
        artist_response = requests.get(
            artist_url,
            headers={"Authorization": f"Bearer {self.access_token}"}
        )

        # Raise an error if the request was unsuccessful
        if artist_response.status_code != 200:
            raise Exception(f"Failed to fetch artist data: {artist_response.status_code} - {artist_response.text}")
        
        # Return the artist's information as a dictionary
        return artist_response.json()
    
# Exercise 3

    def get_artists(self, search_terms):

        rows = []

        for term in search_terms:
            try:
                artist = self.get_artist(term)
                if not isinstance(artist, dict):
                    artist = {}
                    
                rows.append({
                "search_term": term,
                "artist_name": artist.get("name"),
                "artist_id": artist.get("id"),
                "followers_count": artist.get("followers_count")
                })
            except Exception as e:
                print(f"Error fetching data for '{term}': {e}")
                rows.append({
                    "search_term": term,
                    "artist_name": None,
                    "artist_id": None,
                    "followers_count": None
                })
        # Ensure column order is consistent
        df = pd.DataFrame(rows, columns=[
        "search_term",
        "artist_name",
        "artist_id",
        "followers_count"])

        return pd.DataFrame(rows)
