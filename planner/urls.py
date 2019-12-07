from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .models import Meal

urlpatterns = [
 
url(r'^$', views.index, name = 'index'), 
url(r'^admin/', admin.site.urls),
url(r'^lista/', login_required(ListView.as_view(model=Meal)),
        name='lista'),
path('login/', views.login, name = 'login'),
path('logout/',views.logout, name = 'logout'),
path('registration_register/', views.registration_form, name = 'registration_form'),
url(r'^dodaj/$', views.MealCreate.as_view(), name='dodaj'),
]