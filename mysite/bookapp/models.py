from django.db import models

# Create your models here.


class Book(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, default='unknown')
    description = models.CharField(max_length=500)
    rating = models.FloatField()
    image = models.CharField(max_length=500, default="https://www.edmundsgovtech.com/wp-content/uploads/2020/01/default-picture_0_0.png")