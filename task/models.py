from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TaskManager(models.Manager):
    """Ordering by the highest priority"""
    def get_queryset(self):
        return super().get_queryset().order_by('priority')


class Task(models.Model):

    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('very_low', 'Low'),
    ]
    title = models.CharField(max_length=100, default='Untitled')
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=False)  # status of the task Done or Not
    finished_time = models.DateTimeField(auto_now=True, null=True)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default='2')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='tasks', null=True, blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)
    comments = models.TextField(null=True)
    files = models.FileField(max_length=20, null=True)

    objects = TaskManager()

    def __str__(self):
        return self.title
