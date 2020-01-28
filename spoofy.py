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
print(token)