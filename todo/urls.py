from django.urls import path
from .views import TodoListCreate

urlpatterns = [
    path('todos/', TodoListCreate.as_view()),
]
