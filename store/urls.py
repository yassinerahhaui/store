from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_store,name='all_store'),
    path('<int:id>', views.store,name='store1'),
    path('category/<int:id>', views.category,name='category'),
]