from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from book.models import Book, Genre, Author

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'author', 'popular_book')
    list_editable = ('popular_book',)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
