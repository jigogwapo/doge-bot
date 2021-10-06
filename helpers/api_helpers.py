import requests

dadjoke_uri = 'https://icanhazdadjoke.com/'

def get_random_dadjoke():
    dadjoke_json = requests.get(f'{dadjoke_uri}',headers={'Accept': 'application/json'}).json()
    return dadjoke_json['joke']

catfact_uri = 'https://catfact.ninja'

def get_catfact():
    catfact_json = requests.get(f'{catfact_uri}/fact').json()
    return catfact_json['fact']