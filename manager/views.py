from django.shortcuts import render
from django.views import generic

from manager.models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "manager/index.html"
