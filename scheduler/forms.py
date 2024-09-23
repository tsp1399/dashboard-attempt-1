from django import forms
from .models import ContentSchedule

class ContentScheduleForm(forms.ModelForm):
    class Meta:
        model = ContentSchedule
        fields = ['primary_keyword', 'traffic_volume', 'keyword_difficulty']
