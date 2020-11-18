from django.shortcuts import render, redirect, HttpResponse
from .models import Task, Document
from .forms import TaskForm, DocumentForm
import os
from django.conf import settings


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Main page', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def add_task(request):
    error = ""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = "Error! Form was filled incorrectly"

    form = TaskForm()
    context = {
        "form": form,
        "error": error
    }
    return render(request, 'main/add_task.html', context)

def upload_file(request):
    error = ""
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            key = request.POST['description']
            try:
                Document.objects.get(description=key)
                error = "File with this key already exists!"
            except Exception:
                form.save()
                return redirect('home')
    form = DocumentForm()
    return render(request, 'main/upload_file.html', {
        'form': form,
        'error': error,
    })

def find_file(request):
    if 'key' in request.GET:
        key = request.GET['key']
        try:
            file_path = str(Document.objects.get(description=key).document).replace('documents/', '')
            return redirect('find-file/' + file_path)
        except Exception:
             return render(request, 'main/find_file.html', {"error": "There is no file with current key!"})
    else:
        return render(request, 'main/find_file.html')

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, 'documents/' + path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response