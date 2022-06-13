from django.contrib import admin
from .models import *


admin.site.register(Article)

#admin.site.register(ContactRequest)

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
