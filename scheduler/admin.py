from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import ContentSchedule
from django import forms
import csv
from io import TextIOWrapper
from django.contrib.auth.models import User
from django.utils import timezone

class CSVImportForm(forms.Form):
    csv_file = forms.FileField()

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

    change_list_template = 'admin/scheduler/contentschedule/change_list.html'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv, name='scheduler_contentschedule_import_csv'),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            csv_file = TextIOWrapper(csv_file, encoding=request.encoding)
            reader = csv.DictReader(csv_file)
            
            for row in reader:
                # Assuming 'user' in CSV is a username
                user, _ = User.objects.get_or_create(username=row['user'])
                
                ContentSchedule.objects.create(
                    primary_keyword=row['primary_leyword'],  # Note: There's a typo in your CSV header
                    user=user,
                    traffic_volume=int(row['traffic_volume']),
                    keyword_difficulty=int(row['keyword_difficulty']),
                    article_status=row['article_status'],
                    # If you want to set created_at from CSV, uncomment the next line:
                    # created_at=timezone.datetime.strptime(row['created_at'], '%Y-%m-%d %H:%M:%S')
                )
            
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CSVImportForm()
        payload = {"form": form}
        return render(request, "admin/csv_form.html", payload)
