from django.db import models


class Training_Type(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    article = models.TextField(null=True, blank=True)
    image = models.ImageField()
    price = models.DecimalField(decimal_places=2, max_digits=5, null=False, blank=False, default=9.99)

    def __str__(self):
        return self.name
