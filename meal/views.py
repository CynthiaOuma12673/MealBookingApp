from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User
from django.http  import HttpResponseRedirect,Http404
from . forms import UserRegisterForm
from .models import Order,Profile
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.forms.models import model_to_dict
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'all-meals/home.html')

def register(request):
    if request.user.is_authenticated:
    #redirect user to the profile page
        return redirect('home')
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
            
    else:
        form = UserRegisterForm()
    return render(request,"registration/register.html",{'form':form})
