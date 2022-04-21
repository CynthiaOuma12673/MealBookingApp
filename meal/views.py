from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from .forms import *
# Create your views here.

def index(request):

    return render(request, 'all-meals/home.html')


def profile(request):
    current_user = request.user
    profile=Profile.objects.filter(user_id=current_user.id)
    return render(request, 'profile.html', {'profile': profile})


def update_profile(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id=user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('profile')

    return render(request, 'update_profile.html', {"form": form})