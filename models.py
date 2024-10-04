from django.db import models
from django.contrib.auth.models import User  # Importing Django's built-in user model like thing

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One-to-one relationship with Django's User model
    

    #cust_id = models.DecimalField(unique= True, max_digits=10, decimal_places=2, null=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length=128, null=True)  # Consider using Django's User model for password management
   
    def __str__(self):
        return self.user.username  # Returns the username of the linked User object

class Vegetable(models.Model):
    veg_id = models.DecimalField(unique= True, max_digits=10, decimal_places=2, null = True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='vegetables/')
    recipes = models.ManyToManyField('VegetableRecipe', blank=True, related_name='vegetables')

class VegetableRecipe(models.Model):
    vegetable = models.ForeignKey(Vegetable, on_delete=models.CASCADE, related_name='recipe_set')
    recipe_name = models.CharField(max_length=255)
    instructions = models.TextField()

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    vegetables = models.ManyToManyField(Vegetable)
    order_date = models.DateTimeField(auto_now_add=True)
