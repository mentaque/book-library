from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from book.models import Book

User = get_user_model()

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
