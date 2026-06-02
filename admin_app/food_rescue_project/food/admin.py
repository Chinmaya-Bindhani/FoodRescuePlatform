from django.contrib import admin
from .models import FoodDonation

@admin.register(FoodDonation)
class FoodDonationAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'food_type', 'quantity', 'location', 'donor', 'created_at')
    list_filter = ('category', 'food_type')
    search_fields = ('title', 'location', 'description')
