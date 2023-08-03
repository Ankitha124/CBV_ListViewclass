from django.shortcuts import render

# Create your views here.
from app.models import*
from django.views.generic import ListView

class Trainers_list(ListView):
    model=Trainers
    template_name='Trainers_list.html'
    context_object_name='tl'
    #queryset=Trainers.objects.filter(trainer_name='ankitha')
    ordering='trainer_name'

