from django.db import models
import string
import random

# Create your models here.
class Shortener(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.create_short_url(self.long_url)
        super().save(*args, **kwargs)

    @staticmethod
    def create_short_url(long_url):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))

