from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
    path('', views.AddToCartView.as_view(), name='add-to-cart'),
]