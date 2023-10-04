from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from django.utils.translation import gettext_lazy as _
from .models import Trainer, Social
# Register your models here.

class SocialInline(TabularInline):
    model = Social

class SocialAdmin(ModelAdmin):
    list_display = ("name", "link")

class TrainerAdmin(admin.ModelAdmin): 
    list_display = ("firstname", "lastname", "position")
    inlines = [
        SocialInline,
    ]

admin.site.register(Trainer, TrainerAdmin)