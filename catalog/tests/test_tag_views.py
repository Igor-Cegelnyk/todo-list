
from django.test import TestCase
from django.urls import reverse

from catalog.models import Tag


class PublicTagTest(TestCase):
    def setUp(self) -> None:
        Tag.objects.create(name="Test tag")

    def test_tag_page_required(self):
        response = self.client.get(reverse("catalog:tags-list"))

        self.assertEqual(response.status_code, 200)

    def test_tag_create_views(self):
        form_data = {
            "name": "New tag",
        }

        self.client.post(reverse("catalog:tags-create"), data=form_data)
        new_tag = Tag.objects.get(name=form_data["name"])

        self.assertEqual(new_tag.name, form_data["name"])

    def test_tag_update_views(self):
        form_data = {
            "name": "Test tag 2",
        }

        self.client.post(
            reverse("catalog:tags-update", kwargs={"pk": 1}),
            data=form_data
        )
        new_tag = Tag.objects.get(id=1)

        self.assertEqual(new_tag.name, form_data["name"])

    def test_task_delete_views_request(self):
        response = self.client.get(
            reverse("catalog:tags-delete", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "catalog/tags_delete.html"
        )
