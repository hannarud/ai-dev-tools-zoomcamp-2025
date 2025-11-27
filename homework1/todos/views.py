from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import TodoForm
from .models import Todo


class TodoListView(ListView):
    model = Todo
    template_name = "todos/todo_list.html"
    context_object_name = "todos"


class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = "todos/todo_form.html"
    success_url = reverse_lazy("todos:list")


class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = "todos/todo_form.html"
    success_url = reverse_lazy("todos:list")


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "todos/todo_confirm_delete.html"
    success_url = reverse_lazy("todos:list")


class TodoToggleResolvedView(View):
    def post(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.is_resolved = not todo.is_resolved
        todo.save(update_fields=["is_resolved"])
        return redirect("todos:list")
