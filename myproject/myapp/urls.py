from django.urls import path
from .views import SimpleModelListView, SimpleModelDetailView

urlpatterns = [
    path('simple/', SimpleModelListView.as_view(), name='simple_list'),
    path('simple/<int:pk>/', SimpleModelDetailView.as_view(), name='simple_detail'),
]
