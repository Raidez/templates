from django.urls import path
from . import views

app_name = 'todolist'
urlpatterns = [
    path('', views.index, name="index"),
    path('append/', views.add_tast, name="addtask"),
    path('delete/<int:task_id>', views.delete_task, name="deltask")
]
