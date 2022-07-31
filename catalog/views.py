from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from catalog.form import TaskForm
from catalog.models import Task, Tag


class TaskListViews(generic.ListView):
    model = Task
    context_object_name = "tasks_list"
    queryset = Task.objects.all().prefetch_related("tags")
    template_name = "catalog/task_list.html"


class TaskCreateViews(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("catalog:task-list")


class TaskUpdateViews(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("catalog:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("catalog:task-list")
    template_name = "catalog/task_delete.html"


class TagListViews(generic.ListView):
    model = Tag
    context_object_name = "tags_list"
    template_name = "catalog/tags_list.html"


class TagCreateViews(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("catalog:tags-list")


class TagUpdateViews(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("catalog:tags-list")


class TagDeleteViews(generic.DeleteView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("catalog:tags-list")
    template_name = "catalog/tags_delete.html"


def changes_status(request, pk):
    one_task = Task.objects.get(id=pk)
    if one_task.status:
        one_task.status = False
        one_task.save()
    else:
        one_task.status = True
        one_task.save()
    return HttpResponseRedirect(
        reverse_lazy(
            "catalog:task-list",
        )
    )
