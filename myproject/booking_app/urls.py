from django.urls import path
from .views  import (CountrySerializer, UserProfileSerializer, CitySerializer,
                         ServiceSerializer, HotelSerializer, HotelImageSerializer,
                         RoomSerializer, RoomImageSerializer, BookingSerializer, ReviewSerializer)
from rest_framework import routers
router = routers.DefaultRouter()
router.register('users', CountrySerializer)
router.register('users', UserProfileSerializer)
router.register('users', CitySerializer)
router.register('rooms', RoomSerializer)
router.register('services', ServiceSerializer)
router.register('hotels', HotelSerializer)
router.register('hotelImages', HotelImageSerializer)
router.register('roomImages', RoomImageSerializer)
router.register('bookings', BookingSerializer)
router.register('reviews', ReviewSerializer)






