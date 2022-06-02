from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import RegexValidator
import uuid
from django.conf import settings


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


REGEX_PHONE = RegexValidator(r'^(?!0|1|2|3|4|5)[0-9]{10}$', 'Mobile number validator')
PINCODE_VALIDATOR = RegexValidator(r'^[0-9]{6}$', 'Pincode validator')


class CustomUserManager(BaseUserManager):

    def create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError('Please enter a valid Mobile number')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user must be True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super user must be True for is_staff')

        return self.create_user(phone, password, **extra_fields)


class CustomUser(AbstractBaseUser, TimestampedModel, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=10, validators=[REGEX_PHONE], unique=True)
    email = models.EmailField(max_length=130, unique=True)
    name = models.CharField(max_length=120)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)

    last_login = None

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self) -> str:
        return self.name


class UserAddress(TimestampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    house_no = models.CharField(max_length=10)
    street = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50, validators=[PINCODE_VALIDATOR])

    class Meta:
        verbose_name_plural = 'user_addresses'

    def __str__(self):
        return self.user.name
