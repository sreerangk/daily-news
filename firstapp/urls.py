from django.urls import path
from . import views

# Create your views here.

urlpatterns = [
    path('home',views.home, name='home'),
    path('add',views.add,  name='add'),
]