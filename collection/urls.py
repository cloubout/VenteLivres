from django.urls import path
from . import views 

urlpatterns = [
    path('catalog', views.HomeView.as_view(), name='collection'),
    path('catalog/<int:page>/<str:genre>/<int:year>/<int:month>/<str:order>', views.pageCatalogView),
    path('<int:book_id>', views.bookView)
]
