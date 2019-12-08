from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from .models import Task

def index(req: HttpRequest):
	tasks = Task.objects.all()
	return render(req, "todolist/index.html", locals())

def add_tast(req: HttpRequest):
	return redirect('index')

def delete_task(req: HttpRequest, task_id):
	print(task_id)
	return redirect('index')
