from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Url(models.Model):
    url = models.URLField(max_length=255)
    shorten_link = models.URLField(max_length=255)
    slug = models.SlugField(max_length=8, unique=True)

    visits_count = models.PositiveIntegerField(default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'URLs'

    def __str__(self):
        return self.slug