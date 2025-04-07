import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get Spotify credentials from environment
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"

# Replace with your actual playlist URL
playlist_url = "https://open.spotify.com/playlist/1oHlyVGfsuqyCHcMLZFyb8?si=u5gFX8cnTtGwy6Gayu5o_g"
playlist_id = playlist_url.split("/")[-1].split("?")[0]

# Spotify client with OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="playlist-read-private"
))

# Fetch playlist tracks
results = sp.playlist_items(playlist_id)

# Build track list
tracks = []
for item in results["items"]:
    track = item["track"]
    track_name = track["name"]
    artist_name = track["artists"][0]["name"]
    tracks.append(f"{track_name} - {artist_name}")

# Show the result
print("\n🎵 Tracks in Playlist:")
for t in tracks:
    print(t)
