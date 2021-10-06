import requests

base_uri = 'https://icanhazdadjoke.com/'

def get_random_dadjoke():
    dadjoke_json = requests.get(f'{base_uri}',headers={'Accept': 'application/json'}).json()
    return dadjoke_json['joke']