from django.db.models import F
from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer

# Create your views here.


class TaskAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['title', 'deadline']


class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)


class CategoryAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ['name']


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
