from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('donate/', views.create_donation, name='create_donation'),
    path('human-food/', views.human_food, name='human_food'),
    path('human-food/veg/', views.human_veg, name='human_veg'),
    path('human-food/non-veg/', views.human_nonveg, name='human_nonveg'),
    path('animal-food/', views.animal_food, name='animal_food'),
]
