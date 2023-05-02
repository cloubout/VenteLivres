from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from django.db import models
from django.utils.translation import gettext_lazy as _

class SearchForm(forms.Form):
    class Genres(models.TextChoices):
        FANTASY = "FA", _("Fantasy")
        SCIENCE_FICTION = "SF", _("Science Fiction")
        DYSTOPIAN = "DY", _("Dystopian")
        ACTION_ADVENTURE = "AA", _("Action & Adventure")
        MYSTERY = "MY", _("Mystery")
        HORROR = "HO", _("Horror")
        THRILLER = "TH", _("Thriller & Suspense")
        HISTORICAL_FICTION = "HF", _("Historical Fiction")
        ROMANCE = "RO", _("Romance")
        MEMOIR = "ME", _("Memoir & Autobiography")
        BIOGRAPHY = "BI", _("Biography")
        FOOD_DRINK = "FD", _("Food & Drinks")
        ART_PHOTO = "AP", _("Art & Photography")
        SELF_HELP = "SH", _("Self Help")
        HISTORY = "HI", _("History")
        TRAVEL = "TR", _("Travel")
        TRUE_CRIME = "TC", _("True Crime")
        HUMOR = "HU", _("Humor")
        ESSAY = "ES", _("Essay")
        GUIDE = "GU", _("Guide")
        RELIGION_SPIRITUALITY = "RS", _("Religion & Spirituality")
        HUMANITIES_SOCIAL = "HS", _("Humanities & Social sciences")
        PARENTING = "PA", _("Parenting & Families")
        SCIENCE_TECHNOLOGY = "ST", _("Science & Technology")
        CHILDREN ="CH", _("Children's")
        ALL = "AL", _("All")

    genre = forms.ChoiceField(
        choices=Genres.choices,
    )

    after_year = forms.IntegerField(
        validators=[RegexValidator(r"^[0-9]{4}$", "Enter a valid year")],
        required=False,
    )
    before_year = forms.IntegerField(
        validators=[RegexValidator(r"^[0-9]{4}$", "Enter a valid year")],
        required=False,
    )

    text = forms.CharField()
    page = forms.IntegerField(
        required=False,
    )
        
    def is_valid(self):
        self.super().is_valid()
        return self.after_year > self.before_year
