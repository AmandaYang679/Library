from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('libraries/', views.libraries_list, name='libraries'),
    path('library/books/<slug:slug>/', views.books_list_in_library, name='books_in_library'),
    path('books/<slug:slug>/', views.book_detail, name='book_detail'),
    path('all_books/', views.all_books_list, name='all_books'), 
]
