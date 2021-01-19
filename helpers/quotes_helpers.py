import requests

base_uri = 'https://api.quotable.io'

def get_random_quote():
    quote_json = requests.get(f'{base_uri}/random').json()
    quote = {}
    quote['content'] = quote_json['content']
    quote['author'] = quote_json['author']

    return quote

def get_tag_list():
    tag_json = requests.get(f'{base_uri}/tags').json()
    tag_list =[tag['name'] for tag in tag_json]
    tag_list.append('anime')
    return tag_list

def get_random_quote_with_tag(tag):
    quote_json = requests.get(f'{base_uri}/random?tags={tag}').json()
    quote = {}
    quote['content'] = quote_json['content']
    quote['author'] = quote_json['author']

    return quote

def get_random_anime_quote():
    quote_json = requests.get('https://animechanapi.xyz/api/quotes/random').json()
    quote = {}
    quote['content'] = quote_json['data'][0]['quote']
    quote['character'] = quote_json['data'][0]['character']
    quote['anime'] = quote_json['data'][0]['anime']

    return quote