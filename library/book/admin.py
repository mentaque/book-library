from django.contrib import admin

from book.models import Book, Genre, Author


class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
