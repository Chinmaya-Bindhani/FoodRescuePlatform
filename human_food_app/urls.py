from django.urls import path
from .views import human_food_view

urlpatterns = [
    path('', human_food_view, name='human_food'),
]
