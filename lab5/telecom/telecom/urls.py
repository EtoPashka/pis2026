from django.contrib import admin
from django.urls import path, re_path
from calls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.archive, name='archive'),
    path('call/new/', views.create_post, name='create_post'),
    re_path(r'^call/(?P<call_id>\d+)$', views.get_call, name='get_call'),
]