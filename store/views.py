from django.shortcuts import render,redirect
from .models import Store,Category
from django.core.paginator import Paginator
from .forms import ContactForm

# Create your views here.
def all_store(request):
    # all_store = Store.objects.all()
    all_store = Store.objects.order_by('-id')
    category = Category.objects.all()
    paginator = Paginator(all_store, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("store:all_store")
        else:
            form = ContactForm()
    else:
        form = ContactForm()
    context = {
        "stors": page_obj,
        "category": category,
        "form": form,
    }
    return render(request,"all_store.html",context)

def store(request,id):
    store = Store.objects.get(id=id)
    category = Category.objects.all()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("store:all_store")
    else:
        form = ContactForm()
    context = {
        "store": store,
        "category": category,
        "form": form,
    }
    return render(request,'store.html',context)

def category(request,id):
    ct = Store.objects.filter(category=id).order_by('-id')
    category = Category.objects.all()
    paginator = Paginator(ct, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("store:all_store")
    else:
        form = ContactForm()
    context = {
        "stors": page_obj,
        "category": category,
        "form": form,
    }
    return render(request,'filter_by_category.html',context)