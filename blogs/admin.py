from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'date', 'read_time', 'created_at']
    list_filter = ['date', 'created_at']
    search_fields = ['title', 'content']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    
    # Make the form more user-friendly
    fieldsets = (
        ('Post Details', {
            'fields': ('title', 'icon')
        }),
        ('Content', {
            'fields': ('content',)
        }),
        ('Meta Information', {
            'fields': ('date', 'read_time'),
            'classes': ('collapse',)
        }),
    )