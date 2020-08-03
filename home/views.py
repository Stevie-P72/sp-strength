from django.shortcuts import render, get_object_or_404
from profiles.models import UserProfile

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        context = {
                'profile': profile,
            }
        return render(request, 'home/index.html', context)
    return render(request, 'home/index.html')
