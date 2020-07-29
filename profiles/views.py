from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from .forms import UserInfoForm
# Create your views here.


def index(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserInfoForm(instance=profile)
    if request.user.is_authenticated:
        context = {
            'profile': profile,
            'form': form,
        }
        return render(request, 'profiles/index.html', context)
    else:
        return redirect('account_login')
