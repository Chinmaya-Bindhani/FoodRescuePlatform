from django.urls import path
from .views import animal_food_view

urlpatterns = [
    path('', animal_food_view, name='animal_food'),
]
