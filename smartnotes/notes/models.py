from django.db import models


class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateField(auto_now=True)
