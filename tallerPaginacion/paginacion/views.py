from django.shortcuts import render
from django.views.generic import View, ListView
from django.http import HttpResponse

from django.core.paginator import Paginator

from .models import Book
from .tasks import get_books

# Create your views here.

class GetData(View):
    
    def get(self, request):

        url = 'https://silabuzinc.github.io/books/books.json'

        get_books.delay(url)

        return HttpResponse('Subiendo a la db...')
        

class BookList(ListView):
    model = Book
    template_name = 'booklist.html'
    paginate_by = 10


def listing(request):
    books = Book.objects.all()
    paginator = Paginator(books, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'booklist.html', {'page_obj': page_obj})
