from django.contrib.admin.options import ModelAdmin
from semScores.models import CustomUser
from django.contrib import admin

# Register your models here.

class CustomUserAdmin(ModelAdmin):
    search_fields = ("student_id",)


admin.site.register(CustomUser, CustomUserAdmin)