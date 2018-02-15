from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo


def index(request):
    context = {'todos': Todo.objects.all()}
    return render(request, 'index.html', context)


def details(request, id):
    context = {'todo' : Todo.objects.get(id=id)}
    return render(request, 'details.html', context)


def add(request):
    if request.method=='POST':
        todo = Todo(title=request.POST['title'],
                    text=request.POST['text'])
        todo.save()
        return redirect('/todos')
    else:
        return render(request, 'add.html')


def remove(request):
    print('******************')
    print(request.POST.keys())
    if request.method=='POST':
        if 'todo_id' in request.POST.keys():
            delete(request, request.POST['todo_id'])
        else:
            return redirect('/todos')
    context = {'todos':  Todo.objects.all()}
    return render(request, 'remove.html', context)


def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    if request.method !='POST':
        return redirect('/todos')
    return


def update(request, id):
    if request.method=='POST':
        todo = Todo.objects.get(id=id)
        todo.title = request.POST['title']
        todo.text = request.POST['text']
        todo.save(update_fields=['title', 'text'])
        return redirect('/todos')
    else:
        context = {'todo' : Todo.objects.get(id=id)}
        return render(request, 'update.html', context)
