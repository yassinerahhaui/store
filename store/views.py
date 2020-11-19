from django.shortcuts import render
from .models import Store,Category
# Create your views here.
def all_store(request):
    # all_store = Store.objects.all()
    all_store = Store.objects.order_by('-id')
    category = Category.objects.all()
    context = {
        "stors": all_store,
        "category": category,
    }
    return render(request,"all_store.html",context)

def store(request,id):
    store = Store.objects.get(id=id)
    category = Category.objects.all()
    context = {
        "store": store,
        "category": category,
    }
    return render(request,'store.html',context)

def category(request,id):
    ct = Store.objects.filter(category=id).order_by('-id')
    category = Category.objects.all()
    context = {
        "content1": ct,
        "category": category,
    }
    return render(request,'filter_by_category.html',context)