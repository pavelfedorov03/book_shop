from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from books.models import Book


def show_books(request):
    books = Book.objects.all()
    result = ''

    for book in books:
        result += f'<a href="{book.id}">{book.name}</a><hr>'

    return HttpResponse(result)


def show_book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    result = f'{book.name}<hr>Категория: {book.category.name}<hr>Описание книги: {book.description}<hr> Цена: {book.price} рублей'

    return HttpResponse(result)


def show_users(request):
    users = User.objects.all()
    result = 'Все пользователи:<hr>'

    for user in users:
       result += f'{user.username}<br>'

    return HttpResponse(result)

