from django.urls import path

# from .views import *
from .views import get_list, index

urlpatterns = [
    path('', index, name='homie'),
    path('search/', get_list, name='search_results'),
]
