from django.contrib import admin
from . import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn', 'author', 'list_genre']
    list_per_page = 10
    list_filter = ['title']
    search_fields = ['title', 'isbn']
    ordering = ['title']


@admin.register(models.Authors)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth']


# admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Genre)
# admin.site.register(models.Authors)
