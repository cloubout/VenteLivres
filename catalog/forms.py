from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from django.db import models
from django.utils.translation import gettext_lazy as _

from .models import Genres

class SearchForm(forms.Form):
    genre = forms.ChoiceField(choices=Genres.choices)
    after_year = forms.IntegerField(
        validators=[RegexValidator(r"^[0-9]{4}$", "Enter a valid year")],
        required=False,
    )
    before_year = forms.IntegerField(
        validators=[RegexValidator(r"^[0-9]{4}$", "Enter a valid year")],
        required=False,
    )
    text = forms.CharField(required=False)
    page = forms.IntegerField(required=False)
        
        
