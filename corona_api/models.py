from django.db import models

# Create your models here.
class Corona(models.Model):
    title = models.CharField(max_length=255)
    precio = models.IntegerField()
    image = models.URLField()