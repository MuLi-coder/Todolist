from django.shortcuts import render,redirect,get_object_or_404
from .models import Todo
from .forms import TodoForm
# Create your views here.
def todo_list(request):
    todos = Todo.objects.all().order_by('-time')
    return render(request,'todos/todos.html',{'todo':todos})

def todo_add(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()

    return render(request,'todos/todo_add.html',{'form':form})

def todo_delete(request,pk):
    todo_item = get_object_or_404(Todo,pk=pk)

    if request.method == 'POST':
        todo_item.delete()
        return redirect('todo_list')

    return redirect('todo_list')    