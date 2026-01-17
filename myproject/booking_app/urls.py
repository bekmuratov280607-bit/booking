from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserProfileViewSet, ServiceViewSet, CountryViewSet,
    HotelListAPIView, HotelImageViewSet,
    RoomViewSet, RoomImageViewSet,
    BookingViewSet, ReviewViewSet,
    CityListAPIView, CityDetailViewSet,
    HotelDetailAPIView
)

router = DefaultRouter()
router.register('users', UserProfileViewSet)
router.register('services', ServiceViewSet)
router.register('countries', CountryViewSet)
router.register('hotels', HotelListAPIView)
router.register('hotel-images', HotelImageViewSet)
router.register('rooms', RoomViewSet)
router.register('room-images', RoomImageViewSet)
router.register('bookings', BookingViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cities/', CityListAPIView.as_view()),
    path('cities/<int:pk>/', CityDetailViewSet.as_view()),
    path('hotels/<int:pk>/', HotelDetailAPIView.as_view()),
]