from django.shortcuts import render, get_object_or_404, redirect, reverse
from services.models import Training_Type
from .models import PurchaseOrder
from .forms import PurchaseOrderForm
from django.conf import settings

import stripe
# Create your views here.


def checkout(request, article_name):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    article_name = get_object_or_404(Training_Type, name=article_name)
    if request.method == 'POST':
        print(article_name.name)
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'product': article_name.name
        }
        print(form_data)
        order_form = PurchaseOrderForm(form_data)
        if order_form.is_valid():
            print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
            PurchaseOrder = order_form.save()
            request.session['save-personal-info'] = 'save-personal-info' in request.POST
            return redirect(reverse('payment_successful', order.po_ref))
        else:
            print("error")

    else:
        article_name = get_object_or_404(Training_Type, name=article_name)
        purchase_amount = round(article_name.price * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=purchase_amount,
            currency=settings.STRIPE_CURRENCY,
        )

        purchase_order_form = PurchaseOrderForm()
        context = {
            'purchase_order_form': purchase_order_form,
            'article_name': article_name,
            'client_secret': intent.client_secret,
            'stripe_public_key': stripe_public_key
            }
        return render(request, "checkout/index.html", context)


def payment_successful(request, po_ref):
    save_info = request.session.get('save-personal-info')
    order = get_object_or_404(PurchaseOrder, po_ref=po_ref)
    # add success message
    context = {
        'order': order,
    }
    return render(request, 'checkout/payment_successful.html', context)
