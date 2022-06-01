from django.db import models

from users.models import TimestampedModel
from category.models import Category


class Product(TimestampedModel):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='product_images', null=True, blank=True)

    def __str__(self):
        return self.name
