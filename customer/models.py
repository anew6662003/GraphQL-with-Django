from django.db import models


class client(models.Model):
    firs_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)
    
    city = models.CharField(max_length=100)