from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import TaskCreationForm, TagCreationForm
from manager.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "manager/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "manager/task_form.html"
    success_url = reverse_lazy("manager:tasks-list")
    form_class = TaskCreationForm


class TaskDeleteView(generic.DeleteView):
    pass


class TaskUpdateView(generic.UpdateView):
    pass


class TagListView(generic.ListView):
    model = Tag
    template_name = "manager/tag_list.html"


class TagCreationView(generic.CreateView):
    model = Tag
    template_name = "manager/tag_form.html"
    success_url = reverse_lazy("manager:tasks-list")
    form_class = TagCreationForm

# class TagUpdateView(generic.UpdateView):
#     model =