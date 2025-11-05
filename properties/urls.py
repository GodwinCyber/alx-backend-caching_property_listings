from django.urls import path
from .views import property_list, cache_metrics

urlpatterns = [
    path('property-list', property_list, name='property-list'),
    path('cache-metrics/', cache_metrics, name='cache-metrics'),
]

