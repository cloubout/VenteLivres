from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.conf import settings
import datetime

from .models import Book, Author
from members.models import Comment
from .forms import SearchForm
# Create your views here.

class HomeView(generic.ListView):
    """
    View books taht are chosen for the week cover
    """
    template_name = "catalog/home.html"
    model = Book

    def get_queryset(self):
        return Book.objects.filter(weekly_cover=True).all()[:10]

class CatalogView(generic.ListView):
    """
    View of the catalog
    """
    template_name = "catalog/catalog.html"
    model = Book

    def get_queryset(self):
        return Book.objects.order_by('-rating').all()

def search_in_catalog(request):
    num_res = 0
    page_books = []
    if request.method == 'GET':
        form = SearchForm()
    else:
        form = SearchForm(request.POST)
        if form.is_valid():
            search_list = Book.objects.all()
            genre = form.cleaned_data['genre']
            after_year = form.cleaned_data['after_year']
            before_year = form.cleaned_data['before_year']
            lowest_price = form.cleaned_data['lowest_price']
            highest_price = form.cleaned_data['highest_price']
            text = form.cleaned_data['text']
            sort_by = form.cleaned_data['sort_by']
            page = form.cleaned_data['page']

            if genre != "AL":
                search_list = search_list.filter(genre=genre)
            if after_year is None:
                after_year = 1000
            if before_year is None:
                before_year = datetime.date.today().year
            if lowest_price is None:
                lowest_price = 0
            if highest_price is None:
                highest_price = 9999
            if lowest_price > highest_price:
                a = lowest_price
                highest_price = lowest_price
                lowest_price = a
            if text is None:
                text = ""
            if page is None:
                page = 1
                
            search_list = search_list.filter(pub_date__year__gte=after_year, pub_date__year__lte=before_year, title__icontains=text).all()
            search_list = search_list.order_by(sort_by).all()

            num_res = len(search_list)
            max_page = num_res//25
            if num_res%25 > 0:
                max_page+=1
            if page < max_page:
                page_books = searched_list[25*(page-1):25*page]
            elif page == max_page:
                page_books = searched_list[25*(page-1):25*(page-1)+(all_books%25)]

    return render(request, "catalog/search.html", {"form": form, "page_books": page_books, "num_results": num_res})
    
def book_description(request, book_id):
    """
    View for the description of a Book
    """
    b = get_object_or_404(Book, pk=poll_id)
    return render(request, "catalog/book_detail.html", {"book": b})
    
