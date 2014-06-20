"""
switchboard.twiliorouter.admin
-----------------------
twiliorouter Admin.
"""

from django.contrib import admin
from models import Visitor, Message, Recording


class VisitorAdmin(admin.ModelAdmin):
    list_filter = ['user', 'access_code']
    search_fields = ['user', 'access_code']
    list_display = ['user', 'access_code']

admin.site.register(Visitor, VisitorAdmin)
admin.site.register(Message)
admin.site.register(Recording)
