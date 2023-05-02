from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.conf import settings

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

def searchCatalogView(request):
    num_res = 0
    page_books = []
    if request.method == 'GET':
        form = SearchForm()
    else:
        form = SearchForm(request.POST)
        if form.is_valid():
            genre = form.cleaned_data['genre']
            after_year = form.cleaned_data['after_year']
            before_year = form.cleaned_data['before_year']
            text = form.cleaned_data['text']
            page = form.cleaned_data['page']
            search_list = Book.objects.filter(genre=genre, pub_date__year_gte=after_year, pub_date__year_lte=before_year, title__icontains=text).all() 
            num_res = len(search_list)
            max_page = num_res//25
            if num_res%25 > 0:
                max_page+=1
            if page > max_page:
                raise NoMoreResults
            elif page == max_page:
                page_books = searched_list[25*(page-1):25*(page-1)+(all_books%25)]
            else:
                page_books = searched_list[25*(page-1):25*page]
    return render(request, "catalog/search.html", {"form": form, "page_books": page_books, "num_results": num_res})
    
def bookView(request, book_id):
    """
    View for the description of a Book
    """
    b = get_object_or_404(Book, pk=poll_id)
    return render(request, "catalog/book_detail.html", {"book": b})
    
