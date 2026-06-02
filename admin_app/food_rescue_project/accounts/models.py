from django.conf import settings
from django.db import models

class DonorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
