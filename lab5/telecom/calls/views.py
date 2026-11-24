from django.shortcuts import render, redirect
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

def create_post(request):
    if request.user.is_anonymous:
        raise Http404
    else:
        if request.method == "POST":
            form = {
                'city': request.POST.get("city", "").strip(),
                'details': request.POST.get("details", "").strip(),
            }
            if form["city"] and form["details"]:
                if Call.objects.filter(city__iexact=form["city"]).exists():
                    form['errors'] = u"Запись с таким городом уже существует"
                    return render(request, 'create_post.html', {'form': form})

                new_call = Call.objects.create(
                    city=form["city"],
                    details=form["details"],
                    subscriber=request.user
                )
                return redirect('get_call', call_id=new_call.id)
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})