from django.contrib import admin
from users.models import *
# Register your models here.

@admin.register(StudentInfo)
class StudentInfo(admin.ModelAdmin):
    list_display = [field.name for field in StudentInfo._meta.fields]
    search_fields = ('name',)


@admin.register(StudentAcademics)
class StudentAcademics(admin.ModelAdmin):
    list_display = [field.name for field in StudentAcademics._meta.fields]
