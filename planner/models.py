from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):

    kategorie = (
        (Fruit, 'owoce'),
        (Vegetables, 'warzywa'),
        (Dairy_product, 'nabial'),
        (Bakery, 'pieczywo'),
        (Sweets, 'slodycze'),
        (Drinks, 'napoje'),
        (Meat, 'mieso'),
    )
	name = models.CharField(max_length=200)
	category = models.CharField(max_length=200, choices=kategorie, default=Fruit)
	category = models.CharField(max_length=200)
	more_info = models.CharField(max_length=200)
	ccal = models.FloatField()
	protein = models.FloatField()
	fat = models.FloatField()
	carbohyd = models.FloatField()

	def add(self):
		self.save()
	def __str__(self):
		return self.name
