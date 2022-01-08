from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import Room


class Roomform(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
