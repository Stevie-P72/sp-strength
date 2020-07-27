from django.shortcuts import render, get_object_or_404
from .models import Training_Type
# Create your views here.


def services(request):
    types = Training_Type.objects.all()
    context = {
        'types': types,
    }
    return render(request, 'services/index.html', context)


def article(request, type_name):
    article_name = get_object_or_404(Training_Type, pk=type_name)
    context = {
        'article': article_name
    }
    return render(request, 'services/article.html', context)
