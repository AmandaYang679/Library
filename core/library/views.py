from django.shortcuts import render, get_object_or_404
from .models import Library, Book

# Create your views here.
def book_list(request, library_slug=None):
    libraries = Library.objects.all()
    books = Book.objects.filter(available=True)
    
    library = None
    if library_slug:
        library = get_object_or_404(Library, slug=library_slug)
        books = Book.objects.filter(library=library) # первое library - это из models, где ForeignKey, а второе library - это 11 строка
    
    return render(request, 'library/list.html', 
                  {'library': library,
                   'libraries': libraries,
                   'books': books})