from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        CUSTOMER = "customer", "Khách thuê"
        RECEPTIONIST = "receptionist", "Lễ tân"
        TECHNICIAN = "technician", "Kỹ thuật"
        SHOP_OWNER = "shop_owner", "Chủ cửa hàng"
        ADMIN = "admin", "Quản trị"

    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.CUSTOMER)

    class Meta:
        db_table = "users"
