from django.urls import path
from . import views

urlpatterns = [
	path("", views.list_task, name="index"),
	path("add", views.add_task, name="addtask"),
	path("del/<int:id>", views.delete_task, name="deltask")
]
