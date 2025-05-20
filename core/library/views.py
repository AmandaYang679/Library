from django.shortcuts import render, get_object_or_404
from .models import Library, Book

# Create your views here.
# def book_list(request, library_slug=None):
#     libraries = Library.objects.all()
#     books = Book.objects.filter(available=True)
    
#     library = None
#     if library_slug:
#         library = get_object_or_404(Library, slug=library_slug)
#         books = Book.objects.filter(library=library) # первое library - это из models, где ForeignKey, а второе library - это 11 строка
    
#     return render(request, 'library/library.html', 
#                   {'library': library,
#                    'libraries': libraries,
#                    'books': books})


def homepage(request):
    recommended_books = Book.objects.all()[:10]
    return render(request, 'library/homepage.html', {'r_books': recommended_books})


def libraries_list(request):
    libraries = Library.objects.all()
    return render(request, 'library/library_list.html', {'libraries': libraries})


def books_list_in_library(request, slug):
    library = get_object_or_404(Library, slug=slug)
    books = Book.objects.filter(library=library)
    return render(request, 'library/books_in_library.html', {'books': books, 'library': library})
    
    
def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug, available=True)
    return render(request, 'library/book_detail.html', {'book': book})


def all_books_list(request):
    books = Book.objects.all()
    return render(request, 'library/all_books_list.html', {'books': books})
    