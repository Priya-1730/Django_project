from django.shortcuts import render,redirect
from .forms import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

def HomePage(request):
    return render(request, 'home.html')
def ContactUsPage(request):
    return render(request, 'contactus.html')        
def ServicePage(request):
    return render(request, 'service.html')  
def AboutPage(request):
    return render(request, 'about.html')
'''def ProductPage(request):
    context={
        'Product_form':Product_Form()
    }
    if request.method=="POST":
        Product_form=Product_Form(request.POST)
        if Product_form.is_valid():
            Product_form.save()
    return render(request, 'product_add.html', context)'''
'''def AllProduct(request):
   context={
       'products': Product.objects.all()
   }
   return render (request,'product.html',context)'''
'''def DeleteProducts(request,id):
    select_product=Product.objects.get(id=id)
    select_product.delete()
    return redirect('/inventory/products/')'''
'''def ProductUpdate(request,id):
    Select_product=Product.objects.get(id=id)
    context={
        'Product_form':Product_Form(instance=Select_product)
    }
    if request.method=="POST":
            Product_form=Product_Form(request.POST,
            instance=Select_product)
            if Product_form.is_valid():
                Product_form.save()
            return redirect('/inventory/products/')
    return render(request, 'product_add.html', context)'''
class ProductAddView(LoginRequiredMixin,View):

    login_url='/'
    def get(self, request):
        context = {
            'product_form': Product_Form()
        }
        return render(request, 'product_add.html', context)

    def post(self, request):
        product_form = Product_Form(request.POST,request.FILES)

        if product_form.is_valid():
            product_form.save()

        return redirect('/inventory/products/')

class ProductAllView(LoginRequiredMixin,View):
    login_url='/'
    def get(self, request):
        context = {
            'products': Product.objects.all()
        }

        return render(request, 'product.html', context)


class ProductDeleteView(LoginRequiredMixin,View):
    login_url='/'
    def get(self, request, id):
        select_product = Product.objects.get(id=id)
        select_product.delete()

        return redirect('/inventory/products/')


class ProductUpdateView(LoginRequiredMixin,View):
    login_url='/'
    def get(self, request, id):

        select_product = Product.objects.get(id=id)

        context = {
            'product_form': Product_Form(instance=select_product)
        }

        return render(request, 'product_add.html', context)

    def post(self, request, id):

        select_product = Product.objects.get(id=id)

        product_form = Product_Form(
            request.POST,request.FILES,
            instance=select_product
        )

        if product_form.is_valid():
            product_form.save()
            return redirect('/inventory/products/')

        return render(
            request,
            'product_add.html',
            {'product_form': product_form}
        )