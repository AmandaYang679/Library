from django.db import models
from django.urls import reverse

# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    adress = models.TextField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Library'
        verbose_name_plural = 'Libraries'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("library:book_list_by_library", kwargs={"library_slug": self.slug})
    
    
class Book(models.Model):
    library = models.ForeignKey(Library, related_name='books', on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=200)
    image = models.ImageField(upload_to='books/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)

    
    class Meta:
        ordering = ('name',)

    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("library:book_detail", kwargs={"book_slug": self.slug})
    