from django.shortcuts import render
from django.views import View
from .forms import AddToCartForm
from .models import Cart


class AddToCartView(View):
    form_class = AddToCartForm

    def get(self, request, *args, **kwargs):
        user = request.user
        user_cart = user.cart
        if user:
            if user_cart:
                cart = Cart.objects.get(cart=user_cart)
                cart_items = cart.cart_items.all()
                context = {'cart_items': cart_items}
                return render(request, 'cart/cart_items.html', context)
        cart_id = request.session.get('cart_id')
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
            cart_items = cart.cart_items.all()
            context = {'cart_items': cart_items}
            return render(request, 'cart/session_cart.html', context)
        return render(request, 'cart/empty_cart.html')
