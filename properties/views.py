from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Property
from django.http import JsonResponse
from .utils import get_all_properties, get_redis_cache_metrics

# Create your views here.
@cache_page(60 * 15)
def property_list(request):
    '''List all the properties'''
    # properties = Property.objects.all().values(
    #     "id", "title", "description", "price", "location", "created_at"
    # )

    property_data = get_all_properties()

    return JsonResponse({"properties": property_data})

def cache_metrics(request):
    '''Return all the redis both hit and miss metrics'''
    metrics = get_redis_cache_metrics()
    return JsonResponse({"cache_metrics": metrics})
