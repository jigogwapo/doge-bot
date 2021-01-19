import requests

base_uri = 'https://api.quotable.io'

def get_random_quote():
    quote_json = requests.get(f'{base_uri}/random').json()
    quote = {}
    quote['content'] = quote_json['content']
    quote['author'] = quote_json['author']

    return quote