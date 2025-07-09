from django.contrib import admin

from education.models import EducationModel


@admin.register(EducationModel)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "description")
    ordering = ("title",)
