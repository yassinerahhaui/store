from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from store.models import Category
from django.contrib.auth import login as auth_login
from .forms import RegisterForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth import authenticate, login
# Create your views here.

def register(request):
    form = RegisterForm()
    category = Category.objects.all()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('store:all_store')

    context = {
        'form':form,
        "category": category,
    }
    return render(request,'register.html',context)

