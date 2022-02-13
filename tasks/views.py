from django.shortcuts import render, redirect

from tasks.services import get_all_not_done_tasks, mark_task_as_done
from tasks.forms import NewTaskForm


def index(request):
    return render(
        request,
        "index.html",
        {"tasks": get_all_not_done_tasks(), "new_task_form": NewTaskForm()},
    )


def mark_done(request, task_id):
    mark_task_as_done(task_id)
    return redirect("index")


def create_task(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect("index")
