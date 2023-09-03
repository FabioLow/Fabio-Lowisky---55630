from django.contrib import admin
from .models import Movie, Series, Book, Comic

admin.site.register(Movie)
admin.site.register(Series)
admin.site.register(Book)
admin.site.register(Comic)