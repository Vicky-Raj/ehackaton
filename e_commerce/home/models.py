from django.db import models
from django.contrib.auth.models import User

class Images(models.Model):
    image = models.ImageField(upload_to="image")

class Rating(models.Model):
    rating = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    review = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.BooleanField()
    description = models.TextField()
    img = models.ImageField(upload_to="image",blank=True,null=True)
    ratings = models.ManyToManyField(Rating,blank=True)
    def __str__(self):
        return self.name
    

class Category(models.Model):
    category = models.CharField(max_length=100)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.category
    

class Buyer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=10)
    address = models.TextField()
    def __str__(self):
        return self.user.username
    

class Seller(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=10)
    address = models.TextField()
    products = models.ManyToManyField(Product,blank=True)
    def __str__(self):
        return self.user.username

class Quantity(models.Model):
    qty = models.IntegerField()
    product = models.OneToOneField(Product,on_delete=models.CASCADE,blank=True,null=True)

class History(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE)   
    qty = models.IntegerField()
    def __str__(self):
        return self.product.product.name

class Cart(models.Model):
    buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    qty = models.ManyToManyField(Quantity,blank=True)

# class Reviews(models.Model):
#     product = models.OneToOneField(Product,on_delete=models.CASCADE)
#     rating = models.ManyToManyField(Rating,blank=True)

