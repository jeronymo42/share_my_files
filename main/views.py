from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.


def upload(request):
    context = {}

    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        link = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(link)
    return render(request, 'upload.html', context)
