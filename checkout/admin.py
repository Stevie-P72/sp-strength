from django.contrib import admin
from .models import PurchaseOrder
# Register your models here.


class PurchaseOrderAdmin(admin.ModelAdmin):
    readonly_fields = (
        "po_ref", "date", "order_total"
    )
    fields = (
        "po_ref", "date", "first_name",
        "last_name", "email", "product",
        "order_total",
    )
    ordering = ("-date", )


admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
