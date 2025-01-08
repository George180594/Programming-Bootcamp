import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID="26bdd976420b4c46961bb345568055da"
CLIENT_SECRET="8a37a39c7d1847508976a120aa6033a0"
SPOTIFY_DISPLAY_NAME="George Lucas Cunha Rezende"
ID_KEY="12148239057"


# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
date="2024-07-03"
url=f"https://www.billboard.com/charts/hot-100/{date}"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
reponse= requests.get(url=url,headers=header)

website_html= reponse.text
soup=BeautifulSoup(website_html, "html.parser")
titles_tag=soup.select("li ul li h3")
titles_list=[titles.getText().strip() for titles in titles_tag]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="day_46/token.txt",
        username=SPOTIFY_DISPLAY_NAME, 
    )
)
user_id = sp.current_user()["id"]


song_uris = []
year = date.split("-")[0]
for song in titles_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#creating a playlist
playlist = sp.user_playlist_create(user=user_id,name=f"{date} Billboard 100", public=False)

#adding
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)










