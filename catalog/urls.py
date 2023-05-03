from django.urls import path
from . import views 

urlpatterns = [
    path('', views.HomeView.as_view(), name='catalog'),
    path('search', views.search_in_catalog),
    path('<int:book_id>', views.book_description)
]
