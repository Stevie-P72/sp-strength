from django.db import models


class Training_Type(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name
