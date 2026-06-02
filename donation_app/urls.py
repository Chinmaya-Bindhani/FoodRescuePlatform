from django.urls import path
from .views import  donate_view, get_address,nearby_food,claim_food

urlpatterns = [
    path('', donate_view, name='donate'),
    path('claim/<int:donation_id>/', claim_food, name='claim_food'),
    path('get-address/', get_address, name='get_address'),
    path('nearby-food/', nearby_food, name='nearby_food'),

]
