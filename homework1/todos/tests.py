from django.urls import reverse
from django.utils import timezone

from django.test import TestCase

from .models import Todo


class TodoModelTests(TestCase):
    def test_str_returns_title(self):
        todo = Todo.objects.create(title="Finish homework")
        self.assertEqual(str(todo), "Finish homework")

    def test_default_ordering_is_recent_first(self):
        Todo.objects.create(title="First", created_at=timezone.now() - timezone.timedelta(minutes=1))
        latest = Todo.objects.create(title="Second")

        self.assertListEqual(list(Todo.objects.all()), [latest, Todo.objects.get(title="First")])


class TodoViewsTests(TestCase):
    def setUp(self):
        self.todo = Todo.objects.create(title="Sample task")

    def test_list_view_renders_existing_todo(self):
        response = self.client.get(reverse("todos:list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample task")
        self.assertTemplateUsed(response, "todos/todo_list.html")

    def test_create_view_creates_record(self):
        payload = {"title": "New Item", "description": "Details"}
        response = self.client.post(reverse("todos:add"), payload)
        self.assertRedirects(response, reverse("todos:list"))
        self.assertTrue(Todo.objects.filter(title="New Item").exists())

    def test_toggle_resolved_flips_flag(self):
        self.assertFalse(self.todo.is_resolved)
        response = self.client.post(reverse("todos:toggle_resolved", args=[self.todo.pk]))
        self.assertRedirects(response, reverse("todos:list"))
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.is_resolved)

    def test_delete_view_removes_item(self):
        response = self.client.post(reverse("todos:delete", args=[self.todo.pk]))
        self.assertRedirects(response, reverse("todos:list"))
        self.assertFalse(Todo.objects.filter(pk=self.todo.pk).exists())
