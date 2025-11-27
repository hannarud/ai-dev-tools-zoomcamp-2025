from django.urls import path

from .views import (
    TodoCreateView,
    TodoDeleteView,
    TodoListView,
    TodoToggleResolvedView,
    TodoUpdateView,
)

app_name = "todos"

urlpatterns = [
    path("", TodoListView.as_view(), name="list"),
    path("add/", TodoCreateView.as_view(), name="add"),
    path("<int:pk>/edit/", TodoUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", TodoDeleteView.as_view(), name="delete"),
    path("<int:pk>/toggle-resolved/", TodoToggleResolvedView.as_view(), name="toggle_resolved"),
]

