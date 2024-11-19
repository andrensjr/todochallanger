from django.contrib import admin
from .models import Task, Client, Project

class ProjectsInline(admin.TabularInline):
    model = Project
    extra = 0
    max_num = 0

class ClientAdmin(admin.ModelAdmin):
    inlines = [ProjectsInline]

class TasksInline(admin.TabularInline):
    model = Task
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    inlines = [TasksInline]


admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task)