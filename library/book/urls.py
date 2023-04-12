from django.urls import path, include

from book.views import MainView, AuthorView, AllAuthorsListView, BooksListView, BookView, Register, ResetView, \
    ResetDoneView, ResetConfirmView, ResetCompleteView, search

urlpatterns = [
    path('', MainView.as_view(), name='main_page'),
    path('authors/', AllAuthorsListView.as_view(), name='authors_page'),
    path('books/', BooksListView.as_view(), name='books_page'),
    path('authors/<slug:author_slug>/', AuthorView.as_view(), name='author_page'),
    path('books/<slug:book_slug>/', BookView.as_view(), name='book_page'),
    path('users/', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('password_reset/', ResetView.as_view(), name='password_reset'),
    path('password_reset/done/', ResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', ResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset/done/', ResetCompleteView.as_view(), name="password_reset_complete"),
    path('search/', search, name="search-books")
]
