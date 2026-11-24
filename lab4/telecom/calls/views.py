from django.shortcuts import render
from django.http import Http404
from .models import Call

def archive(request):
    return render(request, 'archive.html', {"calls": Call.objects.all()})

def get_call(request, call_id):
    try:
        call = Call.objects.get(id=call_id)
        return render(request, 'call.html', {"call": call})
    except Call.DoesNotExist:
        raise Http404

