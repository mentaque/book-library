from django.urls import path

from book.views import MainView, AuthorView, AllAuthorsListView, BooksListView, BookView

urlpatterns = [
    path('', MainView.as_view(), name='main_page'),
    path('authors/', AllAuthorsListView.as_view(), name='authors_page'),
    path('books/', BooksListView.as_view(), name='books_page'),
    path('authors/<slug:author_slug>/', AuthorView.as_view(), name='author_page'),
    path('books/<slug:book_slug>/', BookView.as_view(), name='book_page'),
]