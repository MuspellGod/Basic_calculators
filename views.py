from django.shortcuts import render, redirect

# Create your views here.
# store/views.py

from rest_framework import viewsets
from .models import Vegetable, VegetableRecipe, Order, Customer
from .serializers import (
    VegetableSerializer,
    VegetableRecipeSerializer,
    OrderSerializer,
    CustomerSerializer
)
from django.contrib.auth import login, authenticate  # Import login and authenticate for handling user sessions
from django.contrib.auth.forms import AuthenticationForm  # Import Django's built-in login form
from .forms import SignUpForm  # Import the custom signup form defined in forms.py

from rest_framework.response import Response # for the cart, added this newly



class VegetableViewSet(viewsets.ModelViewSet):
    queryset = Vegetable.objects.all()
    serializer_class = VegetableSerializer
    

class VegetableRecipeViewSet(viewsets.ModelViewSet):
    queryset = VegetableRecipe.objects.all()
    serializer_class = VegetableRecipeSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# Sign-Up View
def signup_view(request):  # Define a view for handling user registration
    if request.method == 'POST':  # Check if the form is submitted via POST
        form = SignUpForm(request.POST)  # Pass submitted form data to the SignUpForm
        if form.is_valid():  # Check if the submitted form data is valid
            user = form.save()  # Save the new User object (but don't log in yet)
            Customer.objects.create(user=user)  # Create a Customer object linked to this user
            username = form.cleaned_data.get('username')  # Get the username from the form
            password = form.cleaned_data.get('password1')  # Get the first password from the form
            user = authenticate(username=username, password=password)  # Authenticate user
            login(request, user)  # Log the user in (starts a session)
            return redirect('home')  # Redirect to a different page after signup
    else:
        form = SignUpForm()  # If it's a GET request, display a blank form
    return render(request, 'store/signup.html', {'form': form})  # Render the signup template with the form

# Login View
def login_view(request):  # Define a view for logging in existing users
    if request.method == 'POST':  # Check if the form is submitted via POST
        form = AuthenticationForm(request, data=request.POST)  # Pass form data to Django's built-in login form
        if form.is_valid():  # Check if login data is valid (user credentials are correct)
            user = form.get_user()  # Get the authenticated user
            login(request, user)  # Log the user in (starts a session)
            return redirect('home')  # Redirect to a different page after successful login
    else:
        form = AuthenticationForm()  # If it's a GET request, display a blank form
    return render(request, 'store/login.html', {'form': form})  # Render the login template with the form

'''
# testing html page
def vegetable_list(request):
    vegetables = Vegetable.objects.all()
    return render(request, 'store/krishvilla.html', {'vegetables': vegetables})
'''
# for the cart.
class CartViewSet(viewsets.ViewSet):
    def list(self, request):
        cart = request.session.get('cart', [])
        total_price = sum(float(item['price']) for item in cart)
        return Response({'cart': cart, 'total_price': total_price})

    def create(self, request):
        veg_id = request.data.get('veg_id')
        vegetable = Vegetable.objects.get(id=veg_id)
        cart = request.session.get('cart', [])
        cart.append({'id': vegetable.id, 'name': vegetable.name, 'price': str(vegetable.price)})
        request.session['cart'] = cart
        return Response({'message': 'Vegetable added to cart!'})