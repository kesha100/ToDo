from django.urls import path
from .views import TaskAPIView, CategoryAPIView, TaskDetailAPIView, CategoryDetailAPIView


urlpatterns = [
    path('tasks/', TaskAPIView.as_view()),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view()),
    path('categories/', CategoryAPIView.as_view()),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view())
]