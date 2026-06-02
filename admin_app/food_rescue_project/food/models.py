from django.conf import settings
from django.db import models

class FoodDonation(models.Model):
    CATEGORY_CHOICES = [
        ('human', 'Human Food'),
        ('animal', 'Animal Food'),
    ]
    FOOD_TYPE_CHOICES = [
        ('veg', 'Veg'),
        ('nonveg', 'Non-Veg'),
        ('animal', 'Animal Food'),
    ]

    donor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    food_type = models.CharField(max_length=20, choices=FOOD_TYPE_CHOICES)
    quantity = models.PositiveIntegerField()
    location = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} ({self.category})'
