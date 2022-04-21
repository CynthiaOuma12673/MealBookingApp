from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
# Create your views here.


def profile(request):
    current_user = request.user
    profile=Profile.objects.filter(user_id=current_user.id)
    return render(request, 'profile.html', {'profile': profile})