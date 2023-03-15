from django.shortcuts import render
from django.views import View

from book.models import Book, Author


class MainView(View):
    def get(self, request):
        authors = Author.objects.prefetch_related("books").all().order_by("name")
        return render(request, 'index.html', {'authors': authors})

