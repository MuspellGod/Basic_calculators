from django.contrib import admin

# Register your models here.
from .models import Vegetable, Order, VegetableRecipe, Customer

admin.site.register(Vegetable)
admin.site.register(Order)
admin.site.register(Customer)

# Additional stuff to beutify our website
admin.site.register(VegetableRecipe)
