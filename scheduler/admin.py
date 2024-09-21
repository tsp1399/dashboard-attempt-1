from django.contrib import admin
from .models import ContentSchedule

@admin.register(ContentSchedule)
class ContentScheduleAdmin(admin.ModelAdmin):
    list_display = ('primary_keyword', 'user', 'traffic_volume', 'keyword_difficulty', 'article_status', 'created_at')
    list_filter = ('article_status', 'created_at', 'user')
    search_fields = ('primary_keyword',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('primary_keyword', 'user', 'article_status')
        }),
        ('Metrics', {
            'fields': ('traffic_volume', 'keyword_difficulty'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
