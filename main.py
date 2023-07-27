import requests
import spotipy
from bs4 import BeautifulSoup
CLIENT_ID = "5d2c8d3af4b74bf095f34b09d4e026e2"
CLIENT_SECRET = "d32f5c0986c940cf9d7644c23cddb0b8"

urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
from spotipy.oauth2 import SpotifyOAuth

scope = CLIENT_ID

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                    client_secret=CLIENT_SECRET,
                    redirect_uri="https://example.com",
                    scope= "playlist-modify-private"),
                   )



# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])

year  = input('Which year would you like to travel to?Type in this format YYYY-MM-DD: ')

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{year}")

soup = BeautifulSoup(response.text,"html.parser")
title = soup.select("li ul li h3")
# for t in title:
#     print(t.text.split())
song_names = [t.getText().split() for t in title]
names = []

for name in song_names:
    n=""
    for word in name:
        n+=word + " "
    names.append(n)


print(names)
user_id = sp.current_user()["id"]
# print(sp.user_playlists(user=user_id)["items"])
# for i in (sp.user_playlists(user=user_id)["items"]):
#     print(i)
#     if i["name"] ==


uris = []
for n in names:
    results = sp.search(q=f"track:{n} year:{year.split('-')[0]}")
    uris.append(results["tracks"]["items"][0]["uri"])


playlist = sp.user_playlist_create(user=user_id,name=f"{year} Top 100 songs",public=False,description="LOL")

add_tracks = sp.user_playlist_add_tracks(user=user_id,playlist_id=playlist["id"],tracks=uris)

