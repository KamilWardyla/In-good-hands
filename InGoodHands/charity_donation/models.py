from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


INSTITUTION_TYPE = (
    ("Fundacja", "Fundacja"),
    ("Organizacja pozarządowa", "Organizacja pozarządowa"),
    ("Lokalna zbiórka", "Lokalna Zbiórka")
)


class Institution(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    type = models.TextField(choices=INSTITUTION_TYPE, default="Foundation")
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ['type']

    def __str__(self):
        return f"Nazwa instytucji: {self.name}, Typ: {self.type}, Kategoria: {self.categories.all()}"


class Donation(models.Model):
    quantity = models.PositiveSmallIntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=12)
    city = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=16)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
