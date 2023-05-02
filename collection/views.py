from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.conf import settings

from .models import Book, Author
from members.models import Comment
# Create your views here.

class HomeView(generic.ListView):
    """
    View books taht are chosen for the week cover
    """
    template_name = "home.html"
    model = Book

    def get_queryset(self):
        return Book.objects.filter(weekly_cover=True).all()[:10]

class CatalogView(generic.ListView):
    """
    View of the catalog
    """
    template_name = "catalog.html"
    model = Book

    def get_queryset(self):
        return Book.objects.order_by('-rating').all()

def searchCatalogView(request, page, genre, year, month, order):
    searched_books = Book.objects.filter(genre=genre,pub_date__year=year, pub_date__month=month ).order_by('-'+order).all()
    max_page = len(all_books)//25
    if all_books%25 > 0:
        max_page+=1
    page_books = []
    if page > max_page:
        raise NoMoreResults
    elif page == max_page:
        page_books = searched_books[25*page:25*page+(all_books%25)]
    else:
        page_books = searched_books[25*page:25*(page+1)]
    return render(request, "colletion/search.html", {"page_books": page_books})
    
def bookView(request, book_id):
    """
    View for the description of a Book
    """
    b = get_object_or_404(Book, pk=poll_id)
    return render(request, "collection/book_detail.html", {"book": b})
    
