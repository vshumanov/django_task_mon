from tasks.models import Task


def get_all_not_done_tasks():
    return Task.objects.filter(is_done=False)


def get_all_tasks():
    return Task.objects.all()


def mark_task_as_done(task_id):
    task = Task.objects.filter(id=task_id).first()
    if task:
        task.is_done = True
        task.save()
