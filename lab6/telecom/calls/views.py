from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
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

def register(request):
    if request.method == "POST":
        form = {
            'username': request.POST.get("username", "").strip(),
            'email': request.POST.get("email", "").strip(),
            'password': request.POST.get("password", "").strip(),
        }
        if form["username"] and form["email"] and form["password"]:
            try:
                User.objects.get(username=form["username"])
                form['errors'] = u"Пользователь с таким именем уже существует"
                return render(request, 'register.html', {'form': form})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    form["username"],
                    form["email"],
                    form["password"]
                )
                login(request, user)
                return redirect('archive')
        else:
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'register.html', {'form': form})
    else:
        return render(request, 'register.html', {})

def user_login(request):
    if request.method == "POST":
        form = {
            'username': request.POST.get("username", "").strip(),
            'password': request.POST.get("password", "").strip(),
        }
        if form["username"] and form["password"]:
            user = authenticate(username=form["username"], password=form["password"])
            if user is not None:
                login(request, user)
                return redirect('archive')
            else:
                form['errors'] = u"Такого аккаунта не существует или пароль указан неверно"
                return render(request, 'login.html', {'form': form})
        else:
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'login.html', {'form': form})
    else:
        return render(request, 'login.html', {})