from django.db import models


class Training_Type(models.Model):
    name = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name
