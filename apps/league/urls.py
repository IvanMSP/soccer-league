from django.urls import path
from .views import HomeView


urlpatterns = [
    path('inicio/', HomeView.as_view(), name='home_view'),
]