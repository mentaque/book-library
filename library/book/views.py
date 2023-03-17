from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from book.models import Book, Author


class MainView(ListView):
    model = Author
    queryset = Author.objects.all().order_by('name')
    template_name = 'index.html'


class AllAuthorsListView(ListView):
    model = Author
    queryset = Author.objects.all().order_by('name')
    template_name = 'author_list.html'
    context_object_name = 'author_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = self.queryset
        return context


class BooksListView(ListView):
    model = Book
    queryset = Book.objects.all()


class AuthorView(View):
    def get(self, request, author_slug):
        author = Author.objects.get(slug=author_slug)
        return render(request, 'author.html', {'author': author})


class BookView(View):
    def get(self, request, book_slug):
        book = Book.objects.get(slug=book_slug)
        return render(request, 'book.html', {'book': book})
