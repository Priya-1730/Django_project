from .views import *
from django.urls import path

urlpatterns = [
    path('',loginpage),
    path('logout/',logoutuser),
    path('signup/',signuppage),
]