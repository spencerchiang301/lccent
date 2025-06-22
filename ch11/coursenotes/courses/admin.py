from django.contrib import admin
from .models import Course, Note

class NoteInline(admin.TabularInline):
    model = Note
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']
    inlines = [NoteInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Note)
# Register your models here.
