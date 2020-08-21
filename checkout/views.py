from django.shortcuts import render, get_object_or_404, redirect, reverse
from services.models import Training_Type
from .models import PurchaseOrder
from .forms import PurchaseOrderForm
from django.conf import settings
from profiles.models import UserProfile
from profiles.forms import UserInfoForm


import stripe
# Create your views here.


def checkout(request, article_name):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    article_name = get_object_or_404(Training_Type, name=article_name)
    if request.method == 'POST':
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email']
        }
        order_form = PurchaseOrderForm(form_data)
        if order_form.is_valid():
            user = get_object_or_404(UserProfile, user=request.user)
            p = PurchaseOrder(product=article_name,
                              user_profile=user,
                              first_name=request.POST['first_name'],
                              last_name=request.POST['last_name'],
                              email=request.POST['email'],
                              order_total=article_name.price)
            p.save()
            request.session['save-personal-info'] = 'save-personal-info' in request.POST
            request.session['first_name'] = first_name=request.POST['first_name']
            request.session['last_name'] = last_name=request.POST['last_name']
            request.session['email'] = email=request.POST['email']

            seperator = ""

            po_ref = seperator.join(p.po_ref)

            return redirect(reverse('payment_successful', args=[article_name, po_ref]))
        else:
            print("error")

    else:
        try:
            article_is_purchased = PurchaseOrder.objects.get(user_profile=user, product=article_name)
            return redirect('article', article_name=article_name)
        except:
            article_name = get_object_or_404(Training_Type, name=article_name)
            purchase_amount = round(article_name.price * 100)
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                amount=purchase_amount,
                currency=settings.STRIPE_CURRENCY,
            )
            user = get_object_or_404(UserProfile, user=request.user)
            purchase_order_form = PurchaseOrderForm()
            purchase_order_form.fields['first_name'].widget.attrs['value'] = user.first_name
            purchase_order_form.fields['last_name'].widget.attrs['value'] = user.last_name
            purchase_order_form.fields['email'].widget.attrs['value'] = user.email
            context = {
                'purchase_order_form': purchase_order_form,
                'article_name': article_name,
                'client_secret': intent.client_secret,
                'stripe_public_key': stripe_public_key
                }
            return render(request, "checkout/index.html", context)


def payment_successful(request, article_name, po_ref):
    save_info = request.session.get('save-personal-info')
    if save_info:
        profile = get_object_or_404(UserProfile, user=request.user)
        print(profile.first_name)

        profile.first_name = request.session.get('first_name')
        form_data = {
            'first_name': request.session.get('first_name'),
            'last_name': request.session.get('last_name'),
            'email': request.session.get('email')
        }
        UserInfoForm(form_data, instance=profile).save()
    order = get_object_or_404(PurchaseOrder, po_ref=po_ref)
    # add success message
    context = {
        'order': order,
        'po': po_ref
    }

    return render(request, 'checkout/payment_successful.html', context)
