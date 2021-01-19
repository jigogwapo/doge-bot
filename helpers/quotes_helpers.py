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
    tag_list =[tag.name for tag in tag_json]
    return tag_list

def get_random_quote_with_tag(tag):
    quote_json = requests.get(f'{base_uri}/random?tags={tag}').json()
    quote = {}
    quote['content'] = quote_json['content']
    quote['author'] = quote_json['author']

    return quote