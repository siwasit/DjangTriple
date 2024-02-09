from django.urls import path

from . import views

urlpatterns = [
    path("sign-in/", views.sign_in, name="sign-in"),
    path("sign-up/", views.sign_up, name="sign-up"),
    path("sign-out/", views.sign_out, name="sign-out"),
    path("", views.homepage, name="homepage"),
    path("delete/<int:triple_id>", views.triple_delete, name="index"),
    path('edit-triple/<int:triple_id>', views.triple_edit, name='edit_triple'),
]