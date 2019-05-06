# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea
from . import models
from django.forms.models import inlineformset_factory


class ProductForm(ModelForm):

    class Meta:
        model = models.Product
        exclude = ('more_info')
      


PFormSet = inlineformset_factory(
    model=models.Skladnik,
)