from django.shortcuts import render
from .models import DiaryEntry


# Create your views here.
def diary_home(request):
    entries = DiaryEntry.objects.all()
    return render(request, "diary/templates/home.html, {'entries': entries}")
