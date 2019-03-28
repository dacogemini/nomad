import requests

url = "https://sygictravel-sygic-travel-places-v1.p.rapidapi.com/places/list"

headers = {
        "X-RapidAPI-Key": "jUQthuFt2lmshwbhXz4WyDa8bOjsp1TLCXGjsntnJgycI3u0oI"
}

# response = requests.get(url),
response = requests.request("GET", url, headers=headers)

print(response.text)