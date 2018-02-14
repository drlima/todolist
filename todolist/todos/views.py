from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo
# Create your views here.


def index(request):
    context = {
    'name': 'Daniel',
    'todos': Todo.objects.all()[:10]
    }
    return render(request, 'index.html', context)


def details(request, id):
    context = {
        'todo' : Todo.objects.get(id=id)
    }
    return render(request, 'details.html', context)
