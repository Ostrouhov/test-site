from django.db import models

class SearchingUsers(models.Model):
    ByYear = models.CharField(max_length=100)