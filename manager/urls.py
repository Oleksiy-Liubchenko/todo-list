from django.urls import path
from manager.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    TagCreationView
)

app_name = "manager"

urlpatterns = [
    path("", TaskListView.as_view(), name="tasks-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tags-list"),
    path("tags/create/", TagCreationView.as_view(), name="tag-create"),

]
