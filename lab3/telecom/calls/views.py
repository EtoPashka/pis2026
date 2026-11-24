from django.shortcuts import render
from .models import Call

def archive(request):
    return render(request, 'archive.html', {"calls": Call.objects.all()})

