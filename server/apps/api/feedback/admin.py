from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from django.utils.translation import gettext_lazy as _
from .models import Feedback
# Register your models here.


class FeedbackAdmin(ModelAdmin):
    list_display = ("name", "tel", "email")

def has_add_permission(self, request):
    return False

def has_change_permission(self, request, obj=None):
    return False

admin.site.register(Feedback, FeedbackAdmin)
