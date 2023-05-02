from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from .exceptions import BookNotAvailable

from catalog.models import Book

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    inscription_date = models.DateField(auto_now_add=True)
    city_address = models.CharField(max_length=100) 
    postal_code_address = models.IntegerField(
        validators=[RegexValidator(r"^[0-9]{5}", "Enter a valid postal code")],
    )
    street_address = models.CharField(max_length=100)
    street_num_address = models.IntegerField()
    street_num_comp = models.CharField(max_length=100)
    
    phone = models.CharField(
        max_length=14,
        validators=[RegexValidator(r"^0[0-9]([ .-/]?[0-9]{2}){4}$", "Enter a valid phone number.")],
    )
    
    def __str(self):
        return self.first_name

class Order(models.Model):
    class Status(models.TextChoices):
        CREATED = "CR", _("Created")
        SENT = "SE", _("Sent")
        ARRIVED = "AR", _("Arrived")
        
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.CREATED
    )
    books = models.ManyToManyField(Book)

    city_address = models.CharField(max_length=100) 
    postal_code_address = models.IntegerField(
        validators=[RegexValidator(r"^[0-9]{5}$", "Enter a valid postal code")],
    )
    street_address = models.CharField(max_length=100)
    street_num_address = models.IntegerField()
    street_num_comp = models.CharField(max_length=100)
    
    price = models.FloatField()
    
    def __str__(self):
        return self.pk

class Cart(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    books = models.ManyToManyField(Book)

    city_address = models.CharField(max_length=100) 
    postal_code_address = models.IntegerField(
        validators=[RegexValidator(r"^[0-9]{5}$", "Enter a valid postal code")],
    )
    street_address = models.CharField(max_length=100)
    street_num_address = models.IntegerField()
    street_num_comp = models.CharField(max_length=100)
    

    class Shippings(models.TextChoices):
        NORMAL = "NO", _("Normal")
        FAST = "FA", _("Fast")
        ONE_DAY = "OD", _("One day")

    shipping_choice = models.CharField(
        max_length=2,
        choices=Shippings.choices,
        default=Shippings.NORMAL
    )
    price = models.FloatField()
    
    def __str__(self):
        return self.pk

    def add_book(self, book_id):
        book = Book.objects.get(pk=book_id)        
        if book.stocks > book.booked:
            self.price+=book.sell_price
            book.booked+=1
            self.books.add(book)
        else:
            raise BookNotAvailable
        return

    def compute_price(self):
        return 0.0

class Comment(models.Model):
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField(max_length=2000)
    pub_date = models.DateField()

    def __str__(self):
        return self.text[:50]

class Evaluation(models.Model):
    class Ratings(models.IntegerChoices):
        VERY_BAD = 0
        BAD = 1
        OKAY = 2
        GOOD = 3
        VERY_GOOD = 4
        AWESOME = 5
        
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(
        choices=Ratings.choices,
        default=5,
    )
    pub_date = models.DateField()

    def __str__(self):
        return self.rating

    
