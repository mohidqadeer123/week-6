import requests
import pandas as pd

# Exercise 1
# Create class 'Genius'
class Genius:
     def __init__(self, access_token)
        if not access_token:
             raise ValueError("Access token is required to access Genius API")
        self.acesstoken = access_token


# Exercise 2
def get_artist(self, search_term):
   
    """
    Given a search term, search Genius and return the artist object
        for the first hit's primary artist by calling the artist API path.
    """
    # Search Genius for the term
    search_url = f"http://api.genius.com/search?q={search_term}&access_token={self.access_token}&per_page=15"
    resp = requests.get(search_url)
    hits = json_data['response']['hits']
    
    # Get first hit's primary artist ID
    artist_id = hits[0]["result"]["primary_artist"]["id"]

    # Get artist info using that ID
    artist_url = f"http://api.genius.com/artists/{artist_id}?access_token={self.access_token}"
    artist_resp = requests.get(artist_url)
    artist_data = artist_resp.json()["response"]["artist"]

    return artist_data

# Exercise 3
def get_artists(self, search_terms):
    """
    Takes a list of artist search terms, fetches artist information for each one using the Genius API,
     and returns a DataFrame with selected details.
    """
    rows = []

    for term in search_terms:
        artist = self.get_artist(term)
        rows.append({
            "search_term": term,
            "artist_name": artist.get("name"),
            "artist_id": artist.get("id"),
            "followers_count": artist.get("followers_count")

        })

    return pd.DataFrame(rows, columns=["search_term", "artist_name", "artist_id", "followers_count"])



   
  


    
