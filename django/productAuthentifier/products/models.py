from django.db import models
from django import forms

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to= 'pics')

class Batches(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    manufatureDate = models.DateField()
    expiryDate = models.DateField()
    expired = models.BooleanField(default=False)
    code = models.CharField(max_length=100)
    reports = models.IntegerField()

class addProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'company', 'category', 'description')
