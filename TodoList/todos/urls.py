# todos/urls.py
from django.urls import path
from . import views

# 定义本应用内的 URL 模式
urlpatterns = [
    path('', views.todo_list,name = 'todo_list'),
    path('add/', views.todo_add,name = 'todo_add'),
    path('delete/<int:pk>/', views.todo_delete,name='todo_delete' )
]