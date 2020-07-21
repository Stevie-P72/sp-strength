from django.shortcuts import render
from .models import Training_Type
# Create your views here.


def services(request):
    types = Training_Type.objects.all()
    context = {
        'types': types,
    }
    return render(request, 'services/index.html', context)
