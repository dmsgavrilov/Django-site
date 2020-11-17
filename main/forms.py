from .models import Task, Document
from django.forms import ModelForm, Textarea, TextInput, FileField


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ("title", "task",)
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter task name"}),
            "task": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter task description"}),
        }


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document',)
        widgets = {
            "description": TextInput(attrs={
                "placeholder": "Enter file key",
                "class": "form-control",
                "name": "key"
            })
        }