import requests, os
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
base_uri = 'https://www.googleapis.com/books/v1'
book_search_uri = f'/volumes?key={GOOGLE_API_KEY}&q='
default_book_url = 'https://books.google.com.ph/googlebooks/images/no_cover_thumb.gif'

def book_search(book_name):
    book_name = book_name.replace(' ', '+')
    search_data = requests.get(base_uri + book_search_uri + book_name).json()
    if search_data['totalItems'] == 0:
        return None
    else:
        book_data = search_data['items'][0]['volumeInfo']
        book_title = book_data['title']
        book_url = book_data['infoLink']
        book_image = book_data['imageLinks']['thumbnail']
        if 'description' in book_data.keys():
            book_description = book_data['description']
            if len(book_description) > 1000:
                book_description = book_description[:1000]
        else:
            book_description = 'Description is missing.'
        book_author = book_data['authors'][0]
        return {
            "title": book_title,
            "url": book_url,
            "image": book_image,
            "description": book_description,
            "author": book_author
        }

def author_book_search(author):
    author = f'"{author}"'
    search_data = requests.get(f'{base_uri}{book_search_uri}inauthor:{author}&maxResults=5').json()

    author_books = []

    #loop through search_data items and add to a list containing book data
    for i in search_data['items']:
        book = {}
        book_data = i['volumeInfo']
        book['title'] = book_data['title']
        book['url'] = book_data['infoLink']
        if 'imageLinks' in book_data.keys():
            book['image'] = book_data['imageLinks']['thumbnail']
        else:
            book['image'] = default_book_url
        if 'description' in book_data.keys():
            book['description'] = book_data['description']
            if len(book['description']) > 1000:
                book['description'] = book['description'][:1000]
        else:
            book['description'] = 'No description found.'
        author_books.append(book)

    return author_books