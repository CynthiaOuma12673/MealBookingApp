from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User
from django.http  import HttpResponseRedirect,Http404
from . forms import UserRegisterForm, OrderForm, UpdateUserForm, UpdateUserProfileForm
from .models import Oder,Profile
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.forms.models import model_to_dict
from django.contrib import messages

# Create your views here.
def home(request):
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

@login_required(login_url='login')
def order(request):
    current_user=request.user
    order = Oder.objects.all()
    return render(request,"all-meals/order.html",{'order':order,'current_user':current_user})

@login_required(login_url='login')
def new_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.admin = request.user
            order.save()
            return HttpResponseRedirect(reverse("order"))
    else:
        form = OrderForm()
    return render(request, 'all-meals/new_order.html', {'form': form})

@login_required(login_url='login')
def update_order(request,id):
    title = 'UPDATE ORDER'
    instance= Oder.objects.get(id=id)
    if request.method=='POST':
        form = OrderForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()
        messages.success(request, ('Order Updated Successfullly'))
        return redirect('order')
    else:
        form = OrderForm(instance=instance)
    return render(request,'all-meals/new_order.html',{'form':form,'title':title})

@login_required(login_url='login')   
def search_order(request):
    current_user= request.user
    if request.method == 'GET':
        title = request.GET.get("title")
        order = Oder.objects.filter(title__icontains=title).all()

    return render(request, 'all-meals/search.html', {'order': order,'current_user':current_user})

@login_required(login_url='login')
def profile(request, username):
    current_user=request.user
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateUserProfileForm(instance=request.user.profile)

    return render(request, 'all-meals/profile.html', {'user_form':user_form,'profile_form':profile_form})

