'''
Created on 8 Mar 2021

@author: jackm
'''
from django.shortcuts import render, get_object_or_404
from Models import Farm

# url pattern would be
# path('<string:name>/', views.farn, name='farm')

def farm(request, id):
    farm = get_object_or_404(Farm, id=id)
    fields = farm.fields.all()
    template = 'Farm.html'
    context = {'farm' : farm, 'fields' : fields}
    return render(request, template, context)