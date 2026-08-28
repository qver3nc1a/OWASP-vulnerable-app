from django.urls import path
from . import views

urlpatterns = [path("", views.diary_home, name="diary_home")]
