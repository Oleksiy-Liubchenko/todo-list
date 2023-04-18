from django.shortcuts import render
from django.views import generic

from manager.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "manager/index.html"


class TagListView(generic.ListView):
    model = Tag
    template_name = "manager/tag_list.html"

