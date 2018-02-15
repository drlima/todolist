from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo


def index(request):
    context = {
    'name': 'Daniel',
    'todos': Todo.objects.all()
    }
    return render(request, 'index.html', context)


def details(request, id):
    print(type(id))
    context = {
        'todo' : Todo.objects.get(id=id)
    }
    return render(request, 'details.html', context)


def add(request):
    if request.method=='POST':
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()

        return redirect('/todos')
    else:
        return render(request, 'add.html')


def remove(request):
    context = {'todos':  Todo.objects.all()}
    if request.method=='POST':
        todo = Todo.objects.get(id=request.POST['todo_id'])
        todo.delete()
    return render(request, 'remove.html', context)


def update(request, id):
    if request.method=='POST':
        print('*********************************')
        print()
        todo = Todo.objects.get(id=id)
        todo.title = request.POST['title']
        todo.text = request.POST['text']
        todo.save(update_fields=['title', 'text'])
        return redirect('/todos')
    else:
        context = {
            'todo' : Todo.objects.get(id=id)
        }
        return render(request, 'update.html', context)
