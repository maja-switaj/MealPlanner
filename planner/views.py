from django.shortcuts import render
from . import models
 
# Create your views here.
def product_list(request):
    return render(request, 'planner/product_list.html', {})

def login(request):
    return render(request, 'planner/login.html', {})

def logout(request):
    return render(request, 'planner/logout.html', {})

def registration_form(request):
    return render(request, 'planner/registration_form.html', {})