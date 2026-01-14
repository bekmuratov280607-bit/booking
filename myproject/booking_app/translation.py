from modeltranslation.translator import register, TranslationOptions
from .models import( Country, City, Service, Hotel, HotelImage, Room, RoomImage, Booking)


@register(Country)
class CountryTranslation(TranslationOptions):
    fields = ['country_name',]

@register(City)
class CityTranslation(TranslationOptions):
    fields = ['city_name',]

@register(Service)
class ServiceTranslation(TranslationOptions):
    fields = ['service_name',]

@register(Hotel)
class HotelTranslation(TranslationOptions):
    fields = ['hotel_name','description',]

@register(HotelImage)
class HotelImageTranslation(TranslationOptions):
    fields = ['hotel_image',]

@register(Room)
class RoomTranslation(TranslationOptions):
    fields = ['description',]

@register(RoomImage)
class RoomImageTranslation(TranslationOptions):
    fields = ['room_image',]

@register(Booking)
class BookingTranslation(TranslationOptions):
    fields = ['user', 'hotel']
