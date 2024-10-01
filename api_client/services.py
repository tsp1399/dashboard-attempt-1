import requests
import base64
import json
from django.conf import settings
import logging
from .config import DATAFORSEO_LOGIN, DATAFORSEO_PASSWORD, SERPAPI_KEY

logger = logging.getLogger(__name__)

class DataForSEOService:
    def __init__(self):
        self.base_url = "https://api.dataforseo.com/v3"
        self.username = DATAFORSEO_LOGIN
        self.password = DATAFORSEO_PASSWORD

    def get_keyword_data(self, keyword):
        try:
            search_volume_data = self.get_search_volume(keyword)
            keyword_difficulty_data = self.get_keyword_difficulty(keyword)

            result = {
                'search_volume': search_volume_data.get('search_volume'),
                'keyword_difficulty': keyword_difficulty_data.get('keyword_difficulty'),
                'cpc': search_volume_data.get('cpc'),
                'competition': search_volume_data.get('competition'),
                'monthly_searches': search_volume_data.get('monthly_searches')
            }
            logger.info(f"Keyword data received for '{keyword}': {result}")
            return result
        except Exception as e:
            logger.error(f"Error processing DataForSEO API response for '{keyword}': {str(e)}")
            return None

    def get_search_volume(self, keyword):
        endpoint = f"{self.base_url}/keywords_data/clickstream_data/dataforseo_search_volume/live"
        payload = [{
            "location_code": 2036,  # Australia
            "language_code": "en",
            "keywords": [keyword]
        }]

        response = self.make_request(endpoint, payload)
        if response and response.get('tasks') and response['tasks'][0].get('result'):
            result = response['tasks'][0]['result'][0]
            return {
                'search_volume': result.get('search_volume'),
                'cpc': result.get('cpc'),
                'competition': result.get('competition'),
                'monthly_searches': result.get('monthly_searches')
            }
        logger.warning(f"No search volume data found for keyword: {keyword}")
        return {}

    def get_keyword_difficulty(self, keyword):
        endpoint = f"{self.base_url}/dataforseo_labs/google/bulk_keyword_difficulty/live"
        payload = [{
            "keywords": [keyword]
        }]

        response = self.make_request(endpoint, payload)
        if response and response.get('tasks') and response['tasks'][0].get('result'):
            result = response['tasks'][0]['result'][0]
            return {
                'keyword_difficulty': result.get('keyword_difficulty')
            }
        logger.warning(f"No keyword difficulty data found for keyword: {keyword}")
        return {'keyword_difficulty': None}

    def make_request(self, endpoint, payload):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.get_auth_header()}"
        }
        try:
            response = requests.post(endpoint, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()
            if data.get('status_code') == 20000:
                return data
            logger.error(f"Failed to get data. API response: {data}")
            return None
        except requests.exceptions.RequestException as e:
            logger.error(f"Error making request to DataForSEO API: {str(e)}")
            return None

    def get_auth_header(self):
        credentials = f"{self.username}:{self.password}"
        encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
        return encoded_credentials

class SerpAPIService:
    BASE_URL = "https://serpapi.com/search.json"

    def __init__(self):
        self.api_key = SERPAPI_KEY

    def get_search_results(self, query):
        params = {
            'engine': 'google',
            'q': query,
            'location': 'Sydney, New South Wales, Australia',
            'google_domain': 'google.com.au',
            'hl': 'en',
            'gl': 'au',
            'device': 'desktop',
            'api_key': self.api_key
        }
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get('organic_results', [])