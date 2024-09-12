from django.contrib import admin

from djangoApp.models import Message

# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ['content','user']

admin.site.register(Message, MessageAdmin)