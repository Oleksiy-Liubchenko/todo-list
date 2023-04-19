from django.test import TestCase, Client
from django.forms import CheckboxSelectMultiple
from django.urls import reverse_lazy, reverse

from .forms import TaskCreationForm, TagCreationForm
from .models import Task, Tag
from django.utils import timezone


class TaskCreationFormTest(TestCase):
    def test_form_content_label(self):
        form = TaskCreationForm()
        self.assertTrue(form.fields["content"].label == "Content")

    def test_form_deadline_widget_type(self):
        form = TaskCreationForm()

        self.assertTrue(
            form.fields["deadline"].widget.input_type == "datetime-local"
        )

    def test_form_tags_widget_type(self):
        form = TaskCreationForm()

        self.assertTrue(
            isinstance(form.fields["tags"].widget, CheckboxSelectMultiple)
        )


class TagCreationFormTest(TestCase):
    def test_form_tag_name_label(self):
        form = TagCreationForm()
        self.assertTrue(form.fields["name"].label == "Name")

    def test_form_tag_fields_count(self):
        form = TagCreationForm()
        self.assertTrue(len(form.fields) == 1)

    def test_form_tag_model(self):
        form = TagCreationForm()
        self.assertTrue(form.Meta.model == Tag)


class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Test_Tag")

    def test_tag_str_method(self):
        self.assertEqual(str(self.tag), self.tag.name)


class TaskModelTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(content="Test_Task")

    def test_task_str_method(self):
        self.assertEqual(str(self.task), self.task.content)

    def test_task_meta_ordering(self):
        self.assertEqual(Task._meta.ordering, ["status", "-created_at"])


class TaskListViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse_lazy("manager:tasks-list"))

        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse_lazy("manager:tasks-list"))

        self.assertTemplateUsed(response, "manager/index.html")

    def test_pagination_is_five(self):
        for i in range(10):
            Task.objects.create(
                content=f"Task {i}",
                deadline=timezone.now(),
                status=False,
            )
        response = self.client.get(reverse_lazy("manager:tasks-list"))

        self.assertEqual(len(response.context["object_list"]), 5)


class TaskCreateViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/tasks/create/")

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse_lazy("manager:task-create"))

        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse_lazy("manager:task-create"))

        self.assertTemplateUsed(response, "manager/task_form.html")

    def test_form_submission(self):
        form_data = {
            "content": "Test task",
            "deadline": timezone.now(),
        }
        response = self.client.post(reverse_lazy("manager:task-create"), form_data)

        self.assertRedirects(response, reverse_lazy("manager:tasks-list"))


class TaskDeleteViewTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            content="Test task",
            deadline=timezone.now(),
            status=False,
        )

    def test_view_url_accessible_by_name(self):
        response = self.client.get(
            reverse_lazy("manager:task-delete", kwargs={"pk": self.task.pk})
        )

        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(
            reverse_lazy("manager:task-delete", kwargs={"pk": self.task.pk})
        )

        self.assertTemplateUsed(response, "manager/task_confirm_delete.html")

    def test_task_deletion(self):
        response = self.client.post(
            reverse_lazy("manager:task-delete", kwargs={"pk": self.task.pk})
        )

        self.assertRedirects(response, reverse_lazy("manager:tasks-list"))
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())


class TaskUpdateStatusViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.task = Task.objects.create(
            content="Test_Task", status=False
        )

    def test_get_update_task_status(self):
        url = reverse("manager:task-status-update", args=[self.task.id])
        response = self.client.get(url)
        self.task.refresh_from_db()

        self.assertEqual(self.task.status, True)
        self.assertRedirects(response, reverse("manager:tasks-list"))

    def test_post_update_task_status(self):
        url = reverse(
            "manager:task-status-update", args=[self.task.id]
        )
        response = self.client.post(url, {"status": True})

        self.task.refresh_from_db()
        self.assertEqual(self.task.status, True)
        self.assertRedirects(
            response, reverse("manager:tasks-list")
        )


class TagListViewTest(TestCase):
    def test_tag_list_view_uses_correct_template(self):
        response = self.client.get(
            reverse("manager:tags-list")
        )
        self.assertEqual(response.status_code, 200)


class TagCreationViewTest(TestCase):

    def test_tag_create_view(self):
        data = {"name": "Test_Tag"}
        response = self.client.post(
            reverse("manager:tag-create"), data
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tag.objects.count(), 1)
        self.assertEqual(Tag.objects.get().name, "Test_Tag")


class TagUpdateViewTest(TestCase):

    def test_tag_update_view(self):
        tag = Tag.objects.create(name="Test Tag")
        data = {"name": "New_Name"}
        response = self.client.post(
            reverse("manager:tag-update", args=[tag.pk]), data
        )

        self.assertEqual(response.status_code, 302)
        tag.refresh_from_db()
        self.assertEqual(tag.name, "New_Name")


class TagDeleteViewTest(TestCase):

    def test_tag_delete_view(self):
        tag = Tag.objects.create(name="Test Tag")
        response = self.client.post(
            reverse("manager:tag-delete", args=[tag.pk])
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tag.objects.count(), 0)
