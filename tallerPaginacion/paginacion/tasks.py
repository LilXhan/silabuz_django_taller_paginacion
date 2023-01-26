from celery import shared_task
import urllib.request
import json
from .models import Book

@shared_task
def get_books(url_api):

    data = urllib.request.urlopen(url_api)

    books = json.load(data)

    for book in books:
        book.pop('FIELD13')
        book.pop('bookID')

        book['authors'] = book['authors'][:400]

        try:
            book['average_rating'] = float(book['average_rating'])
        except:
            book['average_rating'] = 2.5
        
        try:
            book['num_pages'] = int(book['num_pages'])
        except:
            book['num_pages'] = 100

        
        book['publication_date'] = book['publication_date'].split('/')

        if '/'.join(book['publication_date']) in ['11/31/2000', '6/31/1982']:
            book['publication_date'] = '2023-1-20'
            b = Book.objects.create(**book)
            b.save()
            continue

        if len(book['publication_date']) == 3:
            date = '' #y-m-d
            date += book['publication_date'][2] + '-'
            date += book['publication_date'][0] +  '-'
            date += book['publication_date'][1]
        else:
            date = '2023-1-20'

        book['publication_date'] = date

        b = Book.objects.create(**book)
        b.save()


