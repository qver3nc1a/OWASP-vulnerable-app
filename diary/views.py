from django.shortcuts import render, redirect
from .models import DiaryEntry
from .forms import DiaryEntryForm


# Create your views here.
def diary_home(request):
    if request.method == "GET":
        entries = DiaryEntry.objects.all()
        form = DiaryEntryForm()
        return render(request, "home.html", {"entries": entries, "form": form})
    elif request.method == "POST":
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/diary/")


def entry_page(request, id):
    entry = DiaryEntry.objects.get(id=id)
    return render(request, "entry_page.html", {"entry": entry})
