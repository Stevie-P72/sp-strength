from django.shortcuts import render, get_object_or_404
from services.models import Training_Type
from .forms import PurchaseOrderForm
# Create your views here.


def checkout(request, article_name):
    article_name = get_object_or_404(Training_Type, name=article_name)
    purchase_order_form = PurchaseOrderForm()
    context = {
       'purchase_order_form': purchase_order_form,
       'article_name': article_name,
    }
    return render(request, "checkout/index.html", context)
