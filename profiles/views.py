from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from .forms import UserInfoForm
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        if request.method == 'POST':
            form = UserInfoForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('profiles')

        else:
            form = UserInfoForm(instance=profile)
            context = {
                'profile': profile,
                'form': form,
            }
            return render(request, 'profiles/index.html', context)
    else:

        return redirect('account_login')

