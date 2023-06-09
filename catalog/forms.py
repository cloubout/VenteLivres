from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from django.db import models
from django.utils.translation import gettext_lazy as _

from .models import Genres, SortingMethods

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
    lowest_price=forms.IntegerField(required=False)
    highest_price=forms.IntegerField(required=False)
    text = forms.CharField(required=False)
    sort_by = forms.ChoiceField(choices=SortingMethods.choices)
    page = forms.IntegerField(required=False)
    
