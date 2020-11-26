from django.contrib import admin
from .models import Category,Store,Contact
# Register your models here.
admin.site.register(Store)
admin.site.register(Category)
admin.site.register(Contact)
