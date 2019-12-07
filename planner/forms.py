# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea
from . import models
from django.forms.models import inlineformset_factory


class MealForm(ModelForm):

    class Meta:
        model = models.Meal
        exclude = ('more_info')
    

MealFormSet = inlineformset_factory(
    parent_model=models.Meal,
    model = model.Product
)