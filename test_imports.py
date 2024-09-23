import dataforseo_client
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.models.keywords_data_google_search_volume_live_request_info import KeywordsDataGoogleSearchVolumeLiveRequestInfo
from dataforseo_client.rest import ApiException

print("All imports successful")
print("dataforseo_client version:", dataforseo_client.__version__)
print("KeywordsDataApi:", KeywordsDataApi)
print("KeywordsDataGoogleSearchVolumeLiveRequestInfo:", KeywordsDataGoogleSearchVolumeLiveRequestInfo)
print("ApiException:", ApiException)