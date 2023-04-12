from datetime import timedelta

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.shortcuts import render, redirect
from django.utils.datetime_safe import date
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView

from book.forms import UserCreationForm
from book.models import Book, Author, UserBookRelation, Review


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


class BooksListView(View):
    def get(self, request):
        books = Book.objects.all()
        data = [21, 20, 19, 18, 17]
        context = {
            'books': books,
            'data': data,
        }
        return render(request, 'book/book_list.html', context)


def search(request):
    q = request.GET.get('q', '')
    search_books = Book.objects.filter(title__iregex=q)
    return render(request, 'newlist.html', {'search_books': search_books})

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
        reviews = Review.objects.filter(book=book)[::-1]
        if request.user.is_authenticated:
            relation = UserBookRelation.objects.filter(user=request.user, book=book).exists()
            context = {
                'book': book,
                'relation': relation,
                'reviews': reviews,
            }
        else:
            context = {
                'book': book,
                'reviews': reviews,
            }
        return render(request, 'book.html', context)

    @method_decorator(login_required, name='dispatch')
    def post(self, request, book_slug):
        book = Book.objects.get(slug=book_slug)
        if 'text' in request.POST:
            text = request.POST.get('text')
            Review.objects.create(user=request.user, book=book, text=text)
        else:
            relation = UserBookRelation.objects.filter(user=request.user, book=book)
            if relation.exists():
                relation.delete()
            else:
                UserBookRelation.objects.create(user=request.user, book=book)
        return redirect('book_page', book_slug=book_slug)


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
            'form': form,
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
