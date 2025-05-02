# messaging/admin.py
from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
     list_display = ('sender', 'receiver', 'timestamp', 'is_read')
     list_filter = ('is_read', 'timestamp', 'sender', 'receiver')
     search_fields = ('content', 'sender__username', 'receiver__username')
     readonly_fields = ('sender', 'receiver', 'content', 'timestamp')
     def has_add_permission(self, request):
         return False