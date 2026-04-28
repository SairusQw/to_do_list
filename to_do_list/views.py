from django.urls import reverse_lazy
from django.views import generic

from to_do_list.forms import TaskForm, TagForm
from to_do_list.models import Task, Tag


class IndexView(generic.TemplateView):
    template_name = "to_do_list/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.all()
        context["total_tasks"] = Task.objects.count()
        context["completed_tasks"] = Task.objects.filter(mark=True).count()
        context["pending_tasks"] = Task.objects.filter(mark=False).count()
        context["total_tags"] = Tag.objects.count()
        context["recent_tasks"] = tasks.order_by("-datetime")[:5]

        return context


class TaskListView(generic.ListView):
    model = Task
    template_name = "to_do_list/task_list.html"
    queryset = Task.objects.prefetch_related("tags")

class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "to_do_list/task_form.html"
    success_url = reverse_lazy("todo:task_list")

class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "to_do_list/task_form.html" # Використовуємо ту саму форму
    success_url = reverse_lazy("todo:task_list")

class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "to_do_list/task_confirm_delete.html"
    success_url = reverse_lazy("todo:task_list")

class TagListView(generic.ListView):
    model = Tag
    template_name = "to_do_list/tag_list.html"

class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "to_do_list/tag_form.html"
    success_url = reverse_lazy("todo:tag_list")

class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "to_do_list/tag_form.html"
    success_url = reverse_lazy("todo:tag_list")

class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "to_do_list/tag_confirm_delete.html"
    success_url = reverse_lazy("todo:task_list")


from django.shortcuts import get_object_or_404, redirect
from django.views import View
from .models import Task


class TaskToggleMarkView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)

        task.mark = not task.mark
        task.save()

        return redirect("todo:task_list")
