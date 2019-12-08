from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import Task

def list_task(req: HttpRequest):
	tasks = Task.objects.all()
	return render(req, "todolist/index.html", locals())

def add_task(req: HttpRequest):
	taskname = req.POST.get("taskname", None)
	if taskname:
		Task(name=taskname).save()
	return redirect("index")

def delete_task(req: HttpRequest, id: int):
	get_object_or_404(Task, pk=id).delete()
	return redirect("index")
