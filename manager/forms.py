from django import forms
from django.forms import DateTimeInput

from manager.models import Task, Tag


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
            "deadline": DateTimeInput(attrs={"type": "datetime-local"}),
        }


class TagCreationForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
