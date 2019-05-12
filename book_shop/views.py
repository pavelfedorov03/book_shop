from django.template.loader import render_to_string
from django.shortcuts import HttpResponse

from books.models import Book
from categories.models import Category


def show_main_page(request):
    books = Book.objects.order_by('-id')[:5]
    categories = Category.objects.all()[:5]

    result = render_to_string('index.html', {
        'categories': categories,
        'books': books,
    })

    return HttpResponse(result)


