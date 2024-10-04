
from . import views

# store/urls.py

from django.urls import path, include
from rest_framework import routers
from .views import (
    VegetableViewSet,
    VegetableRecipeViewSet,
    OrderViewSet,
    CustomerViewSet,
    CartViewSet, # for the cart 
)

# for the cart
cart_list = CartViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

# from .views import register # for the account creation

router = routers.DefaultRouter()
router.register(r'vegetables', VegetableViewSet)
router.register(r'recipes', VegetableRecipeViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'customers', CustomerViewSet)
#router.register(r'cart', CartViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    path('signup/', views.signup_view, name='signup'),  # Route for the signup page
    path('login/', views.login_view, name='login'),  # Route for the login page
   # path('krishvilla/',views.vegetable_list)
    path('cart/', cart_list, name='cart'),
]
