from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


CENTERS_CHOICES = (
    ('prg', 'Prague'),
    ('brn', 'Brno'),
)


class Center(models.Model):
    center = models.CharField(
        max_length=6, choices=CENTERS_CHOICES, default='prg')

    def __str__(self):
        return f"{self.center}"


class CenterAdmin(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default='kremes')
    email = models.EmailField(default='test@test.com')
    center = models.ForeignKey(Center, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.email}, {self.first_name}, {self.last_name}"


class Member(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(default='test@test.com')
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name}"
