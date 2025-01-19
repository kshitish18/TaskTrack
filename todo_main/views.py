from django.shortcuts import render
from todo.models import Task

# Create your views here.

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed_tasks = Task.objects.filter(is_completed=True)
    uncompleted_tasks = Task.objects.filter(is_completed=False)
    
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
        'uncomplete_tasks': uncompleted_tasks,
    }
    return render(request, 'home.html', context)