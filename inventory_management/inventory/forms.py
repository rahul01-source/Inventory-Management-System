from django import forms
from .models import *


class Laptopform (forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ('type', 'price', 'status', 'issues')


class Desktopform (forms.ModelForm):
    class Meta:
        model = Desktop
        fields = ('type', 'price', 'status', 'issues')


class Mobileform (forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ('type', 'price', 'status', 'issues')
