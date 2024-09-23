from django.urls import path
from . import views

urlpatterns = [
    path('keyword/<int:schedule_id>/', views.keyword_analytics, name='keyword_analytics'),
]
