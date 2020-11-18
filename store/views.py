from django.shortcuts import render
from .models import Store,Category
# Create your views here.
def all_store(request):
    all_store = Store.objects.all()
    category = Category.objects.all()
    context = {
        "stors": all_store,
        "category": category,
    }
    return render(request,"all_store.html",context)