from django.urls import path
from . import views 

urlpatterns = [
    path('', views.HomeView.as_view(), name='catalog'),
    path('search', views.searchCatalogView),
    path('<int:book_id>', views.bookView)
]
