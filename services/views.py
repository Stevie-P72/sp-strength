from django.shortcuts import render, get_object_or_404, redirect
from .models import Training_Type
from checkout.models import PurchaseOrder
from profiles.models import UserProfile
# Create your views here.


def services(request):
    user = get_object_or_404(UserProfile, user=request.user)
    types = Training_Type.objects.all()
    try:
        purchase_orders = PurchaseOrder.objects.filter(user_profile=user)
        articles_purchased = (item.product for item in purchase_orders)
    except:
        articles_purchased = ['#none']
    context = {
        'types': types,
        'purchased': articles_purchased,
    }
    return render(request, 'services/index.html', context)


def article(request, article_name):
    article_name = get_object_or_404(Training_Type, name=article_name)
    user = get_object_or_404(UserProfile, user=request.user)
    try:
        article_is_purchased = PurchaseOrder.objects.get(user_profile=user, product=article_name)
        context = {
            'article': article_name
        }
        return render(request, 'services/article.html', context)
    except:
        return redirect('checkout', article_name=article_name)
