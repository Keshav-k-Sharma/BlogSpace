from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=10, default='📝', help_text="Emoji icon for the post")
    content = models.TextField()
    date = models.DateField(default=timezone.now)
    read_time = models.IntegerField(default=3, help_text="Estimated reading time in minutes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']  # Most recent first
        
    def __str__(self):
        return self.title
