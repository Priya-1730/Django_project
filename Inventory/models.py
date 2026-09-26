from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100,null=True)
    product_code= models.CharField(max_length=100,null=True)
    price = models.FloatField(null=True)
    gst=models.IntegerField(null=True)
    food_product=models.BooleanField(default=False)
    picture = models.ImageField(null=True, upload_to="images/")
    
    def __str__ (self):
            return self.product_name+""+self.product_code