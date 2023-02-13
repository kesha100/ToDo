from rest_framework import serializers
from .models import Task, Category
import datetime
from .utils import send_task_notification
from user.models import MyUser


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['comments'] = f'comments: ' \
                                     f'{instance.comments}'
        return representation


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'