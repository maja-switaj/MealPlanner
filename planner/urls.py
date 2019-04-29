from django.urls import path, include
from . import views

urlpatterns = [ path('', views.product_list, name = 'product_list'),
path('', views.login, name = 'log in'),
path('',views.logout, name = 'log out'),
path('', views.registration_form, name = 'registration')]