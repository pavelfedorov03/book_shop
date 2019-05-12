from django.shortcuts import HttpResponse
from books.models import Book
from categories.models import Category


def show_categories(request):
    categories = Category.objects.all()
    result = ''

    for category in categories:
        result += f'<a href="{category.id}">{category.name}</a> Всего книг: {category.books.count()}<hr>'

    return HttpResponse(result)


def show_category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    books = category.books.all()
    result = f'{category.name}<hr>'

    for book in books:
        result += f'<a href="{book.id}">{book.name}</a><br>'

    return HttpResponse(result)


def show_book_detail(request, book_id, category_id):
    book = Book.objects.get(id=book_id)
    result = f'{book.name}<hr>Категория: {book.category.name}<hr>Описание книги: {book.description}<hr> Цена: {book.price} рублей'

    return HttpResponse(result)

