from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Todo
from django.contrib.auth.models import User
import datetime
# Create your views here.

# Global datetime variables
year_today = datetime.date.today().year
month_today = datetime.date.today().month
day_today = datetime.date.today().day

def tasksList(request):
    if request.user.is_authenticated:
        tasks = Todo.objects.filter(user=request.user.id)
        not_complete_tasks = tasks.exclude(status='COMPLETE').exclude(deadline=None)
        users = User.objects.all().count()
        choices = Todo.STATUS

        for task in not_complete_tasks:
            if task.deadline.year < year_today or task.deadline.month < month_today or task.deadline.day < day_today:
                task.status = choices[2][0] # EXPIRE STATUS
                task.save() 

        return render(request, 'todoapp/index.html', {
            'tasks': tasks,
            'users': users,
        })
        
    return render(request, 'todoapp/index.html')

def addTask(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            task = Todo(user=request.user, tasks=request.POST['task'])
            task.save()
    return HttpResponseRedirect(reverse('todolist'))

def deleteTask(request, id):
    if request.user.is_authenticated:   
        task = Todo.objects.get(pk=id)
        task.delete()
    return HttpResponseRedirect(reverse('todolist'))

def editTask(request, id):
    message = ""
    task = Todo.objects.get(pk=id)
    choices = Todo.STATUS
    if request.user.is_authenticated:
        if request.method == "POST":

            task.tasks = request.POST['task']
            task.status = request.POST['status']
            # list the str date
            if request.POST['deadline'] != '':
            	date_deadline = list(map(int, request.POST['deadline'].split('-')))
            	if date_deadline[0] > task.date_created.year or date_deadline[1] > task.date_created.month or date_deadline[2] > task.date_created.day:
                	task.deadline = datetime.date(date_deadline[0], date_deadline[1], date_deadline[2])
            	else:
                	message = "Invalid date, must ahead of date created."
                	return render(request, "todoapp/edit.html", {
                    	'task': task,
                    	'message': message,
                    	'choices': choices,
                	})
                	
            task.save()
            return HttpResponseRedirect(reverse('todolist'))
    else:
        message = "Need to login bro."
    return render(request, "todoapp/edit.html", { 
        'task': task,
        'message': message,
        'choices': choices,
    })

    
