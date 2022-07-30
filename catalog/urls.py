from django.urls import path

from catalog.views import (
    TaskListViews,
    TaskCreateViews,
    TaskUpdateViews,
    TaskDeleteView,
    changes_status,
    TagListViews,
    TagCreateViews,
    TagUpdateViews,
    TagDeleteViews,
)

urlpatterns = [
    path(
        "",
        TaskListViews.as_view(),
        name="task-list"
    ),
    path(
        "task/create",
        TaskCreateViews.as_view(),
        name="task-create"
    ),
    path(
        "task/<int:pk>/update",
        TaskUpdateViews.as_view(),
        name="task-update"
    ),
    path(
        "task/<int:pk>/delete",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "<int:pk>/changes/",
        changes_status,
        name="changes-status"
    ),
    path(
        "tags",
        TagListViews.as_view(),
        name="tags-list"
    ),
    path(
        "tags/create",
        TagCreateViews.as_view(),
        name="tags-create"
    ),
    path(
        "tags/<int:pk>/update",
        TagUpdateViews.as_view(),
        name="tags-update"
    ),
    path(
        "tags/<int:pk>/delete",
        TagDeleteViews.as_view(),
        name="tags-delete"
    ),

]


app_name = "catalog"
