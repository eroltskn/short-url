from django.db import models


class UrlHistory(models.Model):
    original_url = models.TextField(unique=True)
    converted_url = models.TextField(unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
