from datetime import datetime

from django.test import TestCase

from catalog.models import Tag, Task


class ModelsTest(TestCase):
    def test_tag_str(self):
        tag = Tag.objects.create(
            name="Test",
        )

        self.assertEqual(
            str(tag), f"{tag.name}"
        )

    def test_task_str(self):
        Tag.objects.create(name="Test tag")
        tag = Tag.objects.all()
        task = Task.objects.create(
            content="test",
            datetime=datetime.now,
            deadline="2022-08-02 16:00:00",
            status=False,
        )
        task.tags.set(tag)
        task.save()

        self.assertEqual(
            str(task),
            f"{task.content} "
            f"(created: {task.datetime}; "
            f"deadline: {task.deadline}; "
            f"status:{task.status}) "
            f"Tags: {task.tags}"
        )

    def test_task_ordering(self):
        for n in range(5, 10):
            Task.objects.create(
                content=f"test {n}",
                datetime=datetime.now,
                deadline=f"2022-08-03 16:00:00",
                status=True,
            )
        for n in range(1, 5):
            Task.objects.create(
                content=f"test {n}",
                datetime=datetime.now,
                deadline=f"2022-08-0{n} 16:00:00",
                status=False,
            )

        tasks = Task.objects.all()
        task_order = tasks.order_by("status", "-datetime")

        self.assertEqual(tasks[0].content, task_order[0].content)
        self.assertEqual(tasks[1].content, task_order[1].content)
        self.assertEqual(tasks[6].content, task_order[6].content)
