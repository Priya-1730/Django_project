from .views import *
from django.urls import path
urlpatterns=[
     path('all/customer/',AllCustomer),
     path('add/customer/',CustomerPage),
     path('customer/delete/<int:id>/',DeleteCustomer,name='Customer_delete'),
     path('customer/update/<int:id>/',UpdateCustomer,name='Customer_update'),
     path('add/orders/',ordersadd),
     path('all/orders/',orderlist),
     path('order/delete/<int:id>/',orderdelete,name='order_delete'),
     path('order/update/<int:id>/',orderupdate,name='order_update')
]