from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

CENTERS = (
        ('prg', 'Praha'),
        ('brn', 'Brno'),
        ('kln', 'Kolin')
        )



class Center(models.Model):
        center = models.CharField(max_length=20, choices=CENTERS, default='prg')

        def __str__(self):
            return self.center



class Member(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})