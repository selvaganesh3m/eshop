from django.forms import ModelForm
from .models import Cart, CartItem


class AddToCartForm(ModelForm):
    class Meta:
        model = Cart
