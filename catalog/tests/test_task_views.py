from datetime import datetime

from django.test import TestCase
from django.urls import reverse

from catalog.models import Tag, Task

TASK_URL = reverse("catalog:task-list")


class PublicTaskTest(TestCase):
    def setUp(self) -> None:
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

    def test_home_page_required(self):
        response = self.client.get(TASK_URL)

        self.assertEqual(response.status_code, 200)

    def test_task_has_context_object_name(self):
        response = self.client.get(TASK_URL)

        self.assertTrue("tasks_list" in response.context)

    def test_task_create_views(self):
        form_data = {
            "content": "Test task",
            "datetime": datetime.now,
            "deadline": "2022-08-02 16:00:00",
            "status": "False",
            "tags": "1"
        }

        self.client.post(reverse("catalog:task-create"), data=form_data)
        new_task = Task.objects.get(content=form_data["content"])

        self.assertEqual(new_task.content, form_data["content"])

    def test_task_update_views(self):
        form_data = {
            "content": "Test task 2",
        }

        self.client.post(
            reverse("catalog:task-update", kwargs={"pk": 1}),
            data=form_data
        )
        new_task = Task.objects.get(id=1)

        self.assertEqual(new_task.content, form_data["content"])

    def test_task_delete_views_request(self):
        response = self.client.get(
            reverse("catalog:task-delete", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "catalog/task_delete.html"
        )

    def test_post_task_delete_views_request(self):
        post_response = self.client.delete(
            reverse("catalog:task-delete", kwargs={"pk": 1})
        )
        self.assertRedirects(post_response, reverse("catalog:task-list"), status_code=302)

    def test_check_the_status_of_the_task(self):
        task = Task.objects.get(id=1)
        response = self.client.get(reverse("catalog:task-list"))
        if task.status:
            self.assertContains(response, "Undo")
        else:
            self.assertContains(response, "Complete")

    def test_post_changes_the_status_of_the_task(self):
        task = Task.objects.get(id=1)

        if task.status:
            self.client.post(reverse("catalog:changes-status", kwargs={"pk": task.id}), data={"status": False})
            new_task = Task.objects.get(id=1)

            self.assertEqual(new_task.status, False)
        else:
            self.client.post(reverse("catalog:changes-status", kwargs={"pk": task.id}), data={"status": True})
            new_task = Task.objects.get(id=1)

            self.assertEqual(new_task.status, True)
