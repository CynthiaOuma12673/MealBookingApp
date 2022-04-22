from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('order/',views.order,name='order'),
    path('new_order/', views.new_order, name='new_order'),
    path('update_order/<id>/', views.update_order, name='update_order'),
    path('search/', views.search_order, name='search'),
    path('profile/<username>/', views.profile, name='profile'),
]