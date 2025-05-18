from django.contrib import admin
from .models import Book, Library

# Register your models here.
@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['name', 'adress']
    prepopulated_fields = {'slug': ('name',)}

    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'available']
    list_filter = ['available', 'library']
    list_editable = ['available']
    prepopulated_fields = {'slug': ('name',)}

