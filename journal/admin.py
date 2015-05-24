from django.contrib import admin

from .models import Student


class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Information', {'fields': ['first_name', 'last_name', 'student_email']}),
        ('School Information', {'fields': ['school_id', 'student_id', 'personal_code'], 'classes': ['collapse']}),
    ]

admin.site.register(Student, StudentAdmin)
