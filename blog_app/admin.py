from django.contrib import admin
from .models import *


admin.site.register(Article)


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False  # disable add in admin dashboard
    
    def has_change_permission(self, request, obj=None):
        return False  # disable edit in admin dashboard
