from apputil import Genius
from pathlib import Path
from dotenv import load_dotenv
import os

# Load environment variables from an .env file
env_path = Path(__file__).with_name("environ.env")
load_dotenv(env_path)  

# Get token from environment
token = os.getenv("ACCESS_TOKEN")

# Initialize Genius client
genius = Genius(token)

# This returns artist info as a dictionary
artist_info = genius.get_artist("Radiohead")