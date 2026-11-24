from django.contrib import admin
from .models import Call

class CallAdmin(admin.ModelAdmin):
    list_display = ('city', 'subscriber', 'get_excerpt', 'call_date')

admin.site.register(Call, CallAdmin)
