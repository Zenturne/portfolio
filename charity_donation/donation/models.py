from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

# Values

FU = 'fu'
OP = 'op'
ZL = 'zb'


# Choices

TYPE_CHOICES = [
    (FU, 'fundacja'),
    (OP, 'organizacja pozarządowa'),
    (ZL, 'zbiórka lokalna'),
]



class Category(models.Model):
    name = models.CharField(max_length=120)

class Institution(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=400, blank=True, null=True)
    type = models.CharField(max_length=24, choices=TYPE_CHOICES)
    categories = models.ManyToManyField(Category)

class Donation(models.Model):
    telephone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')

    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=17, validators=[telephone_regex])
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateTimeField(blank=True, null=True)
    pick_up_comment = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
