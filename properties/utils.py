from django.core.cache import cache
from .models import Property

def get_all_properties():
    '''
    Retrieves all properties from the cache if available
    Otherwise fetches from the database and store it in Redis for 1 Hour.
    '''
    # Checks Redis for all_properties using cache.get('all_properties').
    properties = cache.get('all_properties')
    
    if properties is None:
        properties = Property.objects.all().values(
            "id", "title", "description", "price", "location", "created_at"
        )

        property_data = list(properties)
        cache.set('all_properties', property_data, timeout=3600)
    return property_data



