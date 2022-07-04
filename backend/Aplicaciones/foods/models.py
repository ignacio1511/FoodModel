from django.db import models

# Create your models here.


class FoodImageURL(models.Model):
    image_url = models.CharField(max_length=300)


class Food(models.Model):
    nombre = models.CharField(max_length=70)
    informacion_nutricional = models.TextField(max_length=500)
    image_url = models.ForeignKey(FoodImageURL, blank=False, on_delete=models.CASCADE)
