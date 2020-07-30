from django.db import models
import uuid
from django.conf import settings
from services.models import Training_Type
# Create your models here.


class PurchaseOrder(models.Model):
    po_ref = models.CharField(max_length=16, null=False, editable=False)
    first_name = models.CharField(max_length=40, null=False, blank=False)
    last_name = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField(max_length=256, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Training_Type, null=False, blank=False,
                                on_delete=models.CASCADE)
    order_total = models.DecimalField(max_digits=5, decimal_places=2,
                                      null=False, default=0)

    def _create_po_ref(self):
        return uuid.uuid3().hex.upper()

    def save(self, *args, **kwargs):
        if not self.po_ref:
            self.po_ref = self._create_po_ref()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.po_ref
