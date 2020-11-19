from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_store,name='all_store'),
    path('<int:id>', views.store,name='store'),
    path('category/<int:id>', views.category,name='category'),
]