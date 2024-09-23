from django import forms
from .models import ContentSchedule

class ContentScheduleForm(forms.ModelForm):
    class Meta:
        model = ContentSchedule
        fields = ['primary_keyword', 'traffic_volume', 'keyword_difficulty']
        widgets = {
            'primary_keyword': forms.TextInput(attrs={'required': True}),
            'traffic_volume': forms.NumberInput(attrs={'required': True}),
            'keyword_difficulty': forms.NumberInput(attrs={'required': True}),
        }

class ContentScheduleUpdateForm(forms.ModelForm):
    class Meta:
        model = ContentSchedule
        fields = ['traffic_volume', 'keyword_difficulty']
