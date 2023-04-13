from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def booklist(request):
    return render(request, 'books.html', context={'page':'Book List'})

def addbook(request):
    if request.method == 'POST':
        data = request.POST
        book_name = data.get('book_name')
        book_writer = data.get('book_writer')
        book_description = data.get('book_description')
        image = request.FILES.get('image')
        booksinfo.objects.create(
            book_name = book_name,
            book_description = book_description,
            book_writer = book_writer, 
            image = image,
            )
        return redirect("/")
        
    return render(request, 'addbooks.html', context={'page':'Add Book'})
