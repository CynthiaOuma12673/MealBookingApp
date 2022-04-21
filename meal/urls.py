from django.urls import path
from . import views

urlpatterns=[
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('', views.home, name='home'),
]