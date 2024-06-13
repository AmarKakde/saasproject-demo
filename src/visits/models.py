from django.db import models

# Create your models here.

class PageVisits(models.Model):
    # id -> primary key auto field
    path = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
