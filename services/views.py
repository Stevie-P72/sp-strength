from django.shortcuts import render, get_object_or_404, redirect
from .models import Training_Type
from .forms import ArticleForm, NewArticleForm
from checkout.models import PurchaseOrder
from profiles.models import UserProfile
# Create your views here.


def services(request):
    types = Training_Type.objects.all()
    try:
        user = get_object_or_404(UserProfile, user=request.user)
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
    context = {
                'article': article_name
            }
    if request.user.is_superuser:
        return render(request, 'services/article.html', context)
    else:
        try:
            if request.user.is_authenticated:
                user = get_object_or_404(UserProfile, user=request.user)
            article_is_purchased = PurchaseOrder.objects.get(user_profile=user, product=article_name)
            return render(request, 'services/article.html', context)
        except:
            return redirect('checkout', article_name=article_name)


def create(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = NewArticleForm(request.POST, request.FILES)
            if form.is_valid():
                article_name = form.save()
                return redirect('article', article_name)
            else:
                return redirect('create')
        else:
            form = NewArticleForm()
            context = {
                'form': form
            }
            return render(request, 'services/create.html', context)
    else:
        return redirect('services')


def edit(request, article_name):
    article_name = get_object_or_404(Training_Type, name=article_name)
    context = {
                'article': article_name
            }
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article_name)
            if form.is_valid():
                form.save()
                return redirect('article', article_name)
        else:
            form = ArticleForm(instance=article_name)
        context = {
            'article': article_name,
            'form': form
        }
        return render(request, 'services/edit.html', context)
    else:
        return redirect('article', article_name)


def delete(request, article_name):
    article_name = get_object_or_404(Training_Type, name=article_name)
    if request.user.is_superuser:
        article_name.delete()
    return redirect('services')