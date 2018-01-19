from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from .models import Book # Import table book from models

# Get 
def getBook(request):
    books = Book.objects.all()
    return TemplateResponse(request, 'book/index.html', { "books": books})

def input(request):
    return TemplateResponse(request, 'book/forminput.html')
# Post 
def postBook(request):
    book = Book()
    book.title = request.POST['title']
    book.author = request.POST['author']
    book.date_publish = request.POST['date_publish']
    book.number_of_page = request.POST['number_of_page']
    book.type_of_book = request.POST['type_of_book']
    book.save()
    return redirect('/book')
# delete
def delete(request, id):
    books = Book.objects.get(id=id)
    books.delete()
    return redirect('/book')
# update
def edit(request, id):
    books = Book.objects.get(id=id)
    return TemplateResponse(request, 'book/formedit.html', {"books": books})

def update(request, id):
    book = Book.objects.get(id=id)
    book.title = request.POST['title']
    book.author = request.POST['author']
    book.date_publish = request.POST['date_publish']
    book.number_of_page = request.POST['number_of_page']
    book.type_of_book = request.POST['type_of_book']
    book.save()
    return redirect('/book')