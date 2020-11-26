from django.shortcuts import render
from .models import Store,Category
from django.core.paginator import Paginator
# Create your views here.
def all_store(request):
    # all_store = Store.objects.all()
    all_store = Store.objects.order_by('-id')
    category = Category.objects.all()
    paginator = Paginator(all_store, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "stors": page_obj,
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
    paginator = Paginator(ct, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "stors": page_obj,
        "category": category,
    }
    return render(request,'filter_by_category.html',context)