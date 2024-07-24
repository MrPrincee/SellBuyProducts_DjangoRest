from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    available_for_sale = models.BooleanField(default=False)

    def formatted_float(self):
        return f"{self.price:.2f}"

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    balance = models.FloatField(default=0)


