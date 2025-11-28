from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'project_type', 'city', 'status', 'total_apartments', 'signed_count']
    list_filter = ['status', 'project_type', 'city']
    search_fields = ['name', 'address']
