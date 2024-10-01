print("Loading api_client views")
from django.shortcuts import render
from django.http import JsonResponse
from .services import DataForSEOService, SerpAPIService

# Create your views here.

def test_api(request):
    keyword = request.GET.get('keyword', 'default keyword')
    
    dataforseo_service = DataForSEOService()
    serpapi_service = SerpAPIService()
    
    try:
        dataforseo_result = dataforseo_service.get_keyword_data(keyword)
    except Exception as e:
        dataforseo_result = str(e)
    
    try:
        serpapi_result = serpapi_service.get_search_results(keyword)
    except Exception as e:
        serpapi_result = str(e)
    
    return JsonResponse({
        'dataforseo': dataforseo_result,
        'serpapi': serpapi_result
    })
