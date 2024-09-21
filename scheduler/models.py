from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ContentSchedule(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('scheduled', 'Scheduled'),
        ('published', 'Published'),
        ('failed', 'Failed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    primary_keyword = models.CharField(max_length=255)
    traffic_volume = models.PositiveIntegerField()
    keyword_difficulty = models.PositiveIntegerField()
    article_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Content Schedule'
        verbose_name_plural = 'Content Schedules'

    def __str__(self):
        return f"{self.primary_keyword} ({self.article_status})"