from django.urls import path
from manager.views import TaskListView, TagListView

app_name = "manager"

urlpatterns = [
    path("", TaskListView.as_view(), name="tasks-list"),
    path("tags/", TagListView.as_view(), name="tags-list")
]
