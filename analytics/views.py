from django.shortcuts import render, get_object_or_404
from scheduler.models import ContentSchedule
import requests
from django.conf import settings
import base64
import json

def keyword_analytics(request, schedule_id):
    print("Entering keyword_analytics function")
    schedule = get_object_or_404(ContentSchedule, id=schedule_id, user=request.user)
    
    # Existing SerpApi request
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
        response.raise_for_status()
        search_results = response.json().get('organic_results', [])
    except requests.RequestException as e:
        print(f"Error fetching search results: {e}")
        search_results = []

    # DataForSEO API call
    print("Preparing DataForSEO API call")
    
    # Encode credentials
    credentials = f"{settings.DATAFORSEO_LOGIN}:{settings.DATAFORSEO_PASSWORD}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    
    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/json"
    }
    
    post_data = [{
        "location_name": "United States",
        "language_name": "English",
        "keywords": [schedule.primary_keyword]
    }]
    
    try:
        response = requests.post(
            "https://api.dataforseo.com/v3/keywords_data/google/search_volume/live",
            headers=headers,
            data=json.dumps(post_data)
        )
        response.raise_for_status()
        api_result = response.json()
        
        if api_result["status_code"] == 20000:
            search_volume_data = api_result["tasks"][0]["result"][0]
        else:
            print(f"API Error: {api_result['status_message']}")
            search_volume_data = None
    
    except requests.RequestException as e:
        print(f"Exception when calling DataForSEO API: {e}")
        search_volume_data = None

    context = {
        'schedule': schedule,
        'search_results': search_results,
        'search_volume_data': search_volume_data,
    }
    print("Rendering template")
    return render(request, 'analytics/keyword_analytics.html', context)
