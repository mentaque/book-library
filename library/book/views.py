from datetime import timedelta

from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.shortcuts import render, redirect
from django.utils.datetime_safe import date
from django.views import View
from django.views.generic import ListView

from book.forms import UserCreationForm
from book.models import Book, Author


class MainView(View):
    def get(self, request):
        today = date.today()
        authors = Author.objects.filter(
            date_of_birth__month__gte=today.month,
            date_of_birth__year__lte=today.year,
        ).order_by("date_of_birth__month")[:5]
        books = Book.objects.all().order_by("-id")[:7]
        random_books = Book.objects.all().order_by("?")[:5]
        context = {
            'authors': authors,
            'books': books,
            'random_books': random_books,
        }
        return render(request, 'index.html', context)


class AllAuthorsListView(ListView):
    model = Author
    queryset = Author.objects.all().order_by('name')
    template_name = 'author_list.html'
    context_object_name = 'author_list'


class BooksListView(ListView):
    model = Book
    queryset = Book.objects.all()


class AuthorView(View):
    def get(self, request, author_slug):
        author = Author.objects.get(slug=author_slug)
        popular_books = author.books.filter(popular_book=True)
        context = {
            'author': author,
            'popular_books': popular_books,
        }
        return render(request, 'author.html', context)


class BookView(View):
    def get(self, request, book_slug):
        book = Book.objects.get(slug=book_slug)
        return render(request, 'book.html', {'book': book})


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main_page')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class ResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'


class ResetDoneView(PasswordResetDoneView):
    template_name = 'registration/reset_done.html'


class ResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/reset_confirm.html'


class ResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/reset_complete.html'
