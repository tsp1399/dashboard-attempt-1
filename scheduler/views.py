from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ContentScheduleForm, ContentScheduleUpdateForm
from .models import ContentSchedule
from django.contrib.auth.decorators import login_required

@login_required
def user_dashboard(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            schedule_id = request.POST.get('delete')
            schedule = get_object_or_404(ContentSchedule, id=schedule_id, user=request.user)
            schedule.delete()
            messages.success(request, 'Content schedule deleted successfully.')
        elif 'update' in request.POST:
            schedule_id = request.POST.get('update')
            schedule = get_object_or_404(ContentSchedule, id=schedule_id, user=request.user)
            form = ContentScheduleForm(request.POST, instance=schedule)
            if form.is_valid():
                form.save()
                messages.success(request, 'Content schedule updated successfully.')
        else:
            form = ContentScheduleForm(request.POST)
            if form.is_valid():
                content_schedule = form.save(commit=False)
                content_schedule.user = request.user
                content_schedule.save()
                messages.success(request, 'New content schedule added successfully.')
        return redirect('user_dashboard')
    else:
        form = ContentScheduleForm()

    schedules = ContentSchedule.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'scheduler/user_dashboard.html', {'form': form, 'schedules': schedules})
