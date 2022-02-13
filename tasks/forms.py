from django import forms
from tasks.models import Task


class NewTaskForm(forms.ModelForm):
    name = forms.CharField(max_length=255, help_text="Task name")

    class Meta:
        model = Task
        fields = ("name",)
