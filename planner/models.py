from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.
class Product(models.Model):
    Fruit= 'f'
    Vegetables = 'v'
    Dairy_product = 'd'
    Bakery = 'b'
    Sweets = 's'
    Drinks = 'dd'
    Meat = 'm'

    kategorie = (
        (Fruit, 'owoce'),
        (Vegetables, 'warzywa'),
        (Dairy_product, 'nabial'),
        (Bakery, 'pieczywo'),
        (Sweets, 'slodycze'),
        (Drinks, 'napoje'),
        (Meat, 'mieso'),
    )
    name = models.TextField()
    category = models.TextField(max_length=255, choices=kategorie, default="Fruit")
    more_info = models.TextField(max_length=255)
    kcal = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbohyd = models.FloatField()

    def add(self):
        self.save()
    def __str__(self):
        return self.name
    def __unicode__(self):
        return u'%s' % (self.name)

class Meal(models.Model):
    Breakfast = 'b'
    Second_breakfast = 'sb'
    Lunch = 'l'
    Dinner = 'd'
    Snack = 's'
    nameM = (
        (Breakfast, 'sniadanie'),
        (Second_breakfast, 'Drugie sniadanie'),
        (Lunch, 'Lunch'),
        (Dinner, 'Kolacja'),
        (Snack,'Przekaska'),
        )

    nameM = models.TextField(max_length=200)
    kcal_sum = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name = 'skladniki')

    def add(self):
        self.save()
    def __str__(self):
        return self.nameM
    def __unicode__(self):
        return u'%s' % (self.nameM)

