from django.shortcuts import render, get_object_or_404
from scheduler.models import ContentSchedule  # This import is correct
import requests
from django.conf import settings

# Remove this line:
# from .models import ContentSchedule

def keyword_analytics(request, schedule_id):
    schedule = get_object_or_404(ContentSchedule, id=schedule_id)
    
    # Make the SerpApi request from the server
    api_key = settings.SERPAPI_KEY
    params = {
        'engine': 'google',
        'q': schedule.primary_keyword,
        'location': 'Sydney, New South Wales, Australia',
        'google_domain': 'google.com.au',
        'hl': 'en',
        'gl': 'au',
        'device': 'desktop',
        'api_key': api_key
    }
    
    try:
        response = requests.get('https://serpapi.com/search.json', params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        search_results = response.json().get('organic_results', [])
    except requests.RequestException as e:
        print(f"Error fetching search results: {e}")
        search_results = []

    context = {
        'schedule': schedule,
        'search_results': search_results,
    }
    return render(request, 'analytics/keyword_analytics.html', context)
