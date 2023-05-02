from django.urls import path
from . import views 

urlpatterns = [
    path('catalog', views.HomeView.as_view(), name='home'),
    path('catalog/<int:page>/<str:genre>/<int:year>/<int:month>/<str:order>', views.searchCatalogView),
    path('<int:book_id>', views.bookView)
]
