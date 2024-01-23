from django.db import models


class Article(models.Model):
    text = models.TextField(blank=False, null=False)
    date_posted = models.DateField(auto_now=True)
    subject = models.CharField(max_length=100, blank=False, null=False)
