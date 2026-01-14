from .models import Room
from django_filters import FilterSet

class RoomFilter(FilterSet):
    class Meta:
        model = Room
        fields = {
            'country': ['exact'],
            'genre': ['exact'],
            'director': ['exact'],
        }