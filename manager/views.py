from django.urls import reverse_lazy
from django.views import generic, View
from django.shortcuts import get_object_or_404, redirect

from manager.forms import TaskCreationForm, TagCreationForm
from manager.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "manager/index.html"
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "manager/task_form.html"
    success_url = reverse_lazy("manager:tasks-list")
    form_class = TaskCreationForm


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "manager/task_confirm_delete.html"
    success_url = reverse_lazy("manager:tasks-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "manager/task_form.html"
    success_url = reverse_lazy("manager:tasks-list")
    form_class = TaskCreationForm


class TaskUpdateStatusView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        task.status = request.POST.get("status", not task.status)
        task.save()
        return redirect("manager:tasks-list")


class TagListView(generic.ListView):
    model = Tag
    template_name = "manager/tag_list.html"
    paginate_by = 5


class TagCreationView(generic.CreateView):
    model = Tag
    template_name = "manager/tag_form.html"
    success_url = reverse_lazy("manager:tags-list")
    form_class = TagCreationForm


class TagUpdateView(generic.UpdateView):
    model = Tag
    template_name = "manager/tag_form.html"
    success_url = reverse_lazy("manager:tags-list")
    form_class = TagCreationForm


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "manager/tag_confirm_delete.html"
    success_url = reverse_lazy("manager:tags-list")
