from django.urls import path
from .views import IndexView, TaskListView, TagListView, TaskCreateView, TagCreateView, TaskUpdateView, TaskDeleteView, \
    TagUpdateView, TagDeleteView, TaskToggleMarkView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tasks/", TaskListView.as_view(), name="task_list"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/create/", TaskCreateView.as_view(), name="task_create"),
    path("tags/create/", TagCreateView.as_view(), name="tag_create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tasks/<int:pk>/toggle/", TaskToggleMarkView.as_view(), name="task-toggle-mark"),
]

app_name = 'todo'
