import requests
import os
import csv

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

def last_songs_played():
    song_ids = list()
    song_names = list()
    url = "https://api.spotify.com/v1/me/player/recently-played?limit=50"

    payload  = {}
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer '+token,
    }
    response = requests.request("GET", url, headers=headers, data = payload)

    for item in response.json()['items']:
        song_ids.append(item['track']['id'])
        song_names.append(item['track']['name'])

    return song_ids, song_names

song_ids, song_names = last_songs_played()

print(song_ids, song_names)

rows = zip(song_ids, song_names)

with open('history.csv', "w") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)