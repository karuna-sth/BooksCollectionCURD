from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def booklist(request):
    queryset = booksinfo.objects.all()
    context = {'page':'Book List', 'books': queryset}
    return render(request, 'books.html', context)

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


def deletebook(request, id):
    queryset = booksinfo.objects.get(id = id)
    queryset.delete()
    return redirect("/")