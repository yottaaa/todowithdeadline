from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasksList, name="todolist"),
    path('<int:id>/delete', views.deleteTask, name='deletetask'),
    path('<int:id>/edit', views.editTask, name='edittask'),
    path('add/', views.addTask, name='addtask'),
]