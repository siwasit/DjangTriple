from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("delete/<int:triple_id>", views.triple_delete, name="index"),
    path('edit-triple/<int:triple_id>', views.triple_edit, name='edit_triple'),
]