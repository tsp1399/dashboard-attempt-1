from django.test import TestCase
from django.urls import reverse
from .models import ContentSchedule

# Create your tests here.

class ContentScheduleTests(TestCase):
    def test_delete_content_schedule(self):
        schedule = ContentSchedule.objects.create(primary_keyword="Test", traffic_volume=100, keyword_difficulty=5)
        response = self.client.post(reverse('user_dashboard'), {'delete': schedule.id})
        self.assertEqual(response.status_code, 302)  # Should redirect after deletion
        self.assertFalse(ContentSchedule.objects.filter(id=schedule.id).exists())
