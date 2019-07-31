from django.urls import path, include
from . import views

urlpatterns = [
    path('check/', views.check, name="check"),
    path('checkcode/', views.checkcode, name="checkcode"),
    
]