from django.urls import path
from manager.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    TagCreationView,
    TagUpdateView,
    TagDeleteView,
    TaskUpdateStatusView
)

app_name = "manager"

urlpatterns = [
    path("", TaskListView.as_view(), name="tasks-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/update/status/", TaskUpdateStatusView.as_view(), name="task-status-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tags-list"),
    path("tags/create/", TagCreationView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),

]
