from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from scheduler.models import ContentSchedule

# Create your views here.

@login_required
def keyword_analytics(request, schedule_id):
    schedule = get_object_or_404(ContentSchedule, id=schedule_id, user=request.user)
    context = {
        'schedule': schedule,
    }
    return render(request, 'analytics/keyword_analytics.html', context)
