import requests
import os

def get_access_token():
    author_token = os.getenv("AUTHOR")
    refresh_token = os.getenv("REFRESH_TOKEN")
    url = "https://accounts.spotify.com/api/token"
    payload = "grant_type=refresh_token&refresh_token="+refresh_token
    headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'Authorization': "Basic "+author_token
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.json()['access_token']

token = get_access_token()

def currently_playing_data(token):
    url = "https://api.spotify.com/v1/me/player"
    
    headers = {
        'Authorization': "Bearer "+token,
        'User-Agent': "PostmanRuntime/7.20.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "a08ab93e-9584-4e5e-a22a-ed21a1601c1b,7f4965fc-b93f-4618-bc2f-a7d8b6085555",
        'Host': "api.spotify.com",
        'Accept-Encoding': "gzip, deflate",
        'Cookie': "sp_t=cd80a2e1-d772-43a0-ac51-ad4b85df15be; sp_ab=%7B%222019_04_premium_menu%22%3A%22control%22%7D; spot=%7B%22t%22%3A1580071926%2C%22m%22%3A%22pa%22%2C%22p%22%3Anull%7D",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers)

    artists = response.json()['item']['album']['artists']
    artist_names = list()
   
    for artist in artists:
        artist_names.append(artist['name'])
    return artist_names

musicdata = currently_playing_data(token)

print(musicdata)


