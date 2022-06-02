from django.db import models

from products.models import Product
from users.models import TimestampedModel
from django.conf import settings
from users.models import UserAddress


class Cart(TimestampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    shipping_address = models.ForeignKey(UserAddress, on_delete=models.CASCADE,
                                         related_name='cart_shipping_address',
                                         null=True, blank=True)
    billing_address = models.ForeignKey(UserAddress, on_delete=models.CASCADE,
                                        related_name='cart_billing_address',
                                        null=True, blank=True)
    grand_total = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.id}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f'Cart Item {self.id}'

    def save(self, *args, **kwargs):
        self.total = self.product.price * self.quantity
        super(CartItem, self).save(*args, **kwargs)
