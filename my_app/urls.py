from django.urls import path, include
from .views import home, new_search

urlpatterns = [
    path('', home, name="homepage"),
    path('new_search', new_search, name="new_search")
]
