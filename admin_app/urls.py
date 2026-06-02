from django.urls import path
from .views import admin_page_view

urlpatterns = [
    path('', admin_page_view, name='admin_page'),

]
