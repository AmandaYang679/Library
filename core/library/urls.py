from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<slug:library_slug>/', views.book_list, name='book_list_by_library'),
    path('books/<slug:book_slug>/', views.book_detail, name='book_detail'),
]
