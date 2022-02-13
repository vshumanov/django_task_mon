from django.test import TestCase
from tasks import services as tasks_services
from tasks.models import Task


class TestTaskServices(TestCase):
    def setUp(self):
        done_task = Task(name="done_task", is_done=True).save()
        not_done_task = Task(name="not_done_task").save()

    def test_get_all(self):
        tasks = tasks_services.get_all_tasks()
        self.assertEquals(len(tasks), 2)

    def test_get_not_done_tasks(self):
        tasks = tasks_services.get_all_not_done_tasks()
        self.assertEquals(len(tasks), 1)

    def test_mark_task_as_done(self):
        task = Task.objects.get(name="not_done_task")
        tasks_services.mark_task_as_done(task.id)
        tasks = tasks_services.get_all_not_done_tasks()
        self.assertEquals(len(tasks), 0)

    def test_mark_task_as_done_non_existing(self):
        tasks_services.mark_task_as_done(12345)
        tasks = tasks_services.get_all_not_done_tasks()
        self.assertEquals(len(tasks), 1)
