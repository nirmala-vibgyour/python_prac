from django.db import models
from django.contrib.auth.models import User

MEAL_CATEGORIES = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_course", "Main Course"),
    ("desserts", "Desserts")
)

STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)


class Item(models.Model):
    """ Create your models here which inherits from the Model: class of models: lib """

    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_categories = models.CharField(max_length=200,choices=MEAL_CATEGORIES)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal

