from django.db import models


class Training_Type(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)

    def __str__(self):
        return self.name
