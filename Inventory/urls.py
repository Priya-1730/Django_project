from .views import *
from django.urls import path

urlpatterns = [
    path('home/', HomePage, name='home'),
      path('contactus/', ContactUsPage, name='contactus'),
        path('service/', ServicePage, name='service'),
        path('about/', AboutPage, name='about'),
        path('products/add/', ProductAddView.as_view()),
        path('products/',ProductAllView.as_view()),
        path('products/delete/<int:id>/',ProductDeleteView.as_view(),name='Product_delete'),
        path('products/update/<int:id>/',ProductUpdateView.as_view(),name='Product_update')
  
]