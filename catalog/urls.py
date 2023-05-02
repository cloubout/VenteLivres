from django.urls import path
from . import views 

urlpatterns = [
    path('', views.HomeView.as_view(), name='catalog'),
    path('<int:page>/<str:genre>/<int:year>/<int:month>/<str:order>', views.searchCatalogView),
    path('<int:book_id>', views.bookView)
]
