from django.urls import path

from . import views

urlpatterns = [
    path("sign-in/", views.sign_in, name="sign-in"),
    path("sign-up/", views.sign_up, name="sign-up"),
    path("sign-out/", views.sign_out, name="sign-out"),
    path("", views.homepage, name="homepage"),
    path("delete/<int:triple_id>", views.triple_delete, name="index"),
    path('edit-triple/<int:triple_id>', views.triple_edit, name='edit_triple'),
    #Path ของ Demo Sample 01
    path("demo01_crud/", views.homepage, name="homepage"),
    path("export/", views.rdffile_export, name="rdffile_export"),
    path("import/", views.import_xlsx, name="import_xlsx"),
    path("delete_xlsx/<int:file_number>", views.xlsx_del, name="xlsx_del"),
]