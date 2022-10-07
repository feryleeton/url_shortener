import random
import string

from shortener import models


def get_urls():
    return models.Url.objects.all()


def generate_random_slug():
    while True:
        slug = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))
        if not models.Url.objects.filter(slug=slug):
            return slug
