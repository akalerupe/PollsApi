from django.contrib import admin
from .models import Choice,Poll

# Register your models here.
admin.site.register(Choice,Poll)
admin.site.register(Poll)