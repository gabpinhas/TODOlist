from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.views.generic.list import ListView


def tasklist(ListView):
    return HttpResponse('TO Do list')

