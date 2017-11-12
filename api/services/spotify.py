
# Spotify URLS
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)
from .main import load_lyrics
import requests, base64, os
from datetime import timedelta
from django.utils import timezone
from django.core.cache import cache

#Client Keys
CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

class SpotifyService:

    def get_current_song(self, access_token):

        # Auth Step 6: Use the access token to access Spotify API
        authorization_header = {"Authorization":"Bearer {}".format(access_token)}

        # Get profile data
        user_profile_api_endpoint = "{}/me/player/currently-playing".format(SPOTIFY_API_URL)
        response = requests.get(user_profile_api_endpoint, headers=authorization_header)
        if response.status_code == 204:
            return {
                'lyrics' : 'You are not playing any song.'
            }
        if response.status_code != 200:
            raise Exception(response.json())

        data = response.json()

        song_name = data['item']['name']
        first_artist = data['item']['artists'][0]
        artist_name = first_artist['name']
     
        key = "{}-{}".format(song_name, artist_name)
        if cache.get(key, None) is not None:
            return {
                'lyrics' : cache.get(key)
            }
        lyrics = load_lyrics(artist_name, song_name)[0]
        if lyrics == 'Error: Could not find lyrics.':
            lyrics = load_lyrics(artist_name, song_name)[0]
        cache.set(key,lyrics, 3000)
        return {
            'lyrics' : lyrics
        }

    def refresh_token(self, token):
        expires_at = token.expires_at
        refresh_token = token.token_secret
        now = timezone.now()
        if(now >= expires_at):
            encoded_header = ("{}:{}".format(CLIENT_ID, CLIENT_SECRET)).encode('utf-8')
            encoded_header = base64.b64encode(encoded_header)
            encoded_header = encoded_header.decode('utf-8')

            authorization_header = {"Authorization":"Basic {}".format(encoded_header)}
            data = { 'refresh_token' : refresh_token, 'grant_type' : 'refresh_token' }
            
            response = requests.post(SPOTIFY_TOKEN_URL, headers=authorization_header, data=data)
            if response.status_code != 200:
                raise Exception(response.json())
            data = response.json()
            access_token = data['access_token']
            expires_in = data['expires_in']
            now += timedelta(seconds=expires_in)
            token.expires_at = now
            token.token = access_token
            token.save()
            return token.token
        return token.token
            


    def get_current_song_lyrics(self, user):
        social_account = user.socialaccount_set.first()
        social_token = social_account.socialtoken_set.first()
        access_token = self.refresh_token(social_token)
        data = self.get_current_song(access_token)
        return data