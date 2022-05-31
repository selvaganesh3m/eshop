from django.db import models
from users.models import TimestampedModel


class Category(TimestampedModel):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
