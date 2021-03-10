'''
Created on 8 Mar 2021

@author: jackm
'''
from django.db import models
import datetime 

class Farm(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Field(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='fields')
    name = models.CharField(max_length=100)
    size = models.IntegerField(default=None)
    product = models.CharField(max_length=100)
    last_rested = models.DateField(default=datetime.date.today())
    
    def __str__(self):
        return self.product
    