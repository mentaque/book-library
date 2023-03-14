from django.urls import path

from book.views import MainView

urlpatterns = [
    path('', MainView.as_view(), name='main_view')
]