from django.urls import path
from . import views

urlpatterns = [
    path("", views.diary_home, name="diary_home"),
    path("entry/<int:id>/", views.entry_page, name="entry_page"),
    path("entry/<int:id>/edit/", views.edit_entry, name="edit_entry"),
]
