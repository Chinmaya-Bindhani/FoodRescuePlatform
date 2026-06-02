from django.db import models
from register_app.models import Donor


class Donation(models.Model):
    FOOD_FOR_CHOICES = [
        ('human', 'Human Food'),
        ('animal', 'Animal Food'),
    ]
    FOOD_TYPE_CHOICES = [
        ('veg', 'Veg'),
        ('nonveg', 'Non-Veg'),
    ]

    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, related_name='donations')
    food_for = models.CharField(max_length=10, choices=FOOD_FOR_CHOICES)
    food_type = models.CharField(max_length=10, choices=FOOD_TYPE_CHOICES)
    food_name = models.CharField(max_length=150)
    quantity = models.PositiveIntegerField(default=1)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='donation_images/', blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.food_name

class Claim(models.Model):
    donor = models.ForeignKey('register_app.Donor', on_delete=models.CASCADE)
    donation = models.ForeignKey('donation_app.Donation', on_delete=models.CASCADE)
    category = models.CharField(max_length=20)   # veg / nonveg / animal
    claimed_at = models.DateTimeField(auto_now_add=True)

