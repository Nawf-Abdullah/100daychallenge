from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


response = requests.get('https://www.billboard.com/charts/hot-100/2000-08-12')
contents= response.text

soup = BeautifulSoup(contents,'html.parser')
songs = [song.getText() for song in soup.find_all(name='span',class_="chart-element__information__song text--truncate color--primary")]

Client_ID = 'fc081b7d47c2409597ed7290b05faafb'
Client_Secret = '1beb1a89dbff47048ca89ef19cc05824'



sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=Client_ID,
        client_secret=Client_Secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
year = '2000'
song_uris = []

for song in songs:
	result = sp.search(q=f'track:{song} year:{year}',type='track')
	try:
		uri = result['tracks']['items'][0]['uri']
		song_uris.append(uri)
	except IndexError:
		print(f'{song} Skipped')

playlist = sp.user_playlist_create(user=user_id, name=f"2000-11-2 Billboard 100", public=False)
sp.playlist_add_items(playlist_id = playlist['id'],items = song_uris)