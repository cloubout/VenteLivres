from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import datetime

# Create your models here.



class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    biography = models.TextField()
    photo = models.ImageField(upload_to="author_headshots")
    
    class Meta:
        ordering = ["-last_name"]

    def __str__(self):
        return self.first_name+', '+self.last_name

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    mail = models.EmailField(max_length=254)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name
    
class Book(models.Model):
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
        UNKNOWN = "UN", _("Unknown")

    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    pub_date = models.DateField()
    synopsis = models.TextField()
    genre = models.CharField(
        max_length=2,
        choices=Genres.choices,
        default=Genres.UNKNOWN
    )
    cover_photo = models.ImageField(upload_to="book_covers")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    rating = models.FloatField()
    num_rating = models.PositiveIntegerField()
    num_comments = models.PositiveIntegerField()
    weekly_cover = models.BooleanField(default=False)
    sell_price = models.FloatField()
    init_price = models.FloatField()
    stocks = models.PositiveIntegerField()
    booked = models.PositiveIntegerField()
    
    class Meta:
        ordering = ["-title"]
    
    def __str__(self):
        return self.title

    def compute_margin(self):
        return self.sell_price - self.init_price

    def stocks_available(self):
        if self.stocks > 10 :
            return "Available"
        elif self.stocks < 4:
            return "There are only "+str(self.stocks)+" remaining"
        else:
            return "Less than 10 copies available"

    def update_rating(self):
        c = self.evaluation_set.count()
        if c > 0:
            self.rating = 1.0*sum(self.evaluation_set)/c
            self.num_rating = c

