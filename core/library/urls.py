from django.urls import path
from . import views

urlpatterns = [
    path('<slug:library_slug>/', views.book_list, name='book_list'),
]
