from django.urls import path, include
from . import views

urlpatterns = [
 path('', views.product_list, name = 'product_list'),
 url(r'^lista/', login_required(ListView.as_view(model=Product)),
        name='lista'),
path('login/', views.login, name = 'login'),
path('logout/',views.logout, name = 'logout'),
path('registration_register/', views.registration_form, name = 'registration_form'),
url(r'^dodaj/$', views.ProductCreate.as_view(), name='dodaj'),
]