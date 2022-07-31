from django.test import TestCase
from django import forms

from catalog.form import TaskForm
from catalog.models import Tag


class FormsTests(TestCase):
    def test_task_form_field_queryset(self):
        form = TaskForm()
        self.assertQuerysetEqual(
            form.fields["tags"].queryset,
            Tag.objects.all()
        )

    def test_task_form_field_tags_is_model_multiple_choice(self):
        form = TaskForm()
        self.assertTrue(
            form.fields["tags"],
            forms.ModelMultipleChoiceField
        )

    def test_task_form_tags_field_required(self):
        form = TaskForm()
        self.assertEqual(
            form.fields["tags"].required, False
        )
