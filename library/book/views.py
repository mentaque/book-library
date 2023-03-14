from django.shortcuts import render
from django.views import View

from book.models import Book


class MainView(View):
    def get(self, request):
        book = Book.objects.all()
        return render(request, 'index.html', {'book': book})

