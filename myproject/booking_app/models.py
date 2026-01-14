from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class Country(models.Model):
    country_image = models.ImageField(upload_to='flags/')
    country_name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.country_name

class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MaxValueValidator(80), MinValueValidator(18)],
                                           null=True, blank=True)
    user_image = models.ImageField(upload_to='user_photo/', null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    RoleChoices = (
        ('client', 'client'),
        ('owner', 'owner'),

    )
    role = models.CharField(max_length=20, choices=RoleChoices, default='client')
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.role}'

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=40)
    city_image = models.ImageField(upload_to='city_image')

    def __str__(self):
        return f'{self.country}, {self.city_name}'


class Service(models.Model):
    service_image = models.ImageField(upload_to='service_image')
    service_name = models.CharField(max_length=40)

    def __str__(self):
        return self.service_name



class Hotel(models.Model):
    hotel_name = models.CharField(max_length=40)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_hotels')
    hotel_stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 11)],
                                                   null=True, blank=True)
    street = models.CharField(max_length=40)
    postal_code = models.PositiveSmallIntegerField(verbose_name='почтовый индекс')
    description = models.TextField()
    service = models.ManyToManyField(Service)

    def __str__(self):
        return self.hotel_name




class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    hotel_image = models.ImageField(upload_to='hotel_image')

    def __str__(self):
        return f'{self.hotel}, {self.hotel_image}'


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    RoomTypeChoice = (
    ('Люкс', 'Люкс'),
    ("Семенный", "Семенный"),
    ("Стандарт", "Стандарт"),
    ("Двухместный", "Двухместный"))
    room_type = models.CharField(max_length=20, choices=RoomTypeChoice)
    RoomStatusChoice = (
    ("занят", "занят"),
    ("забронирован", "забронирован"),
    ("свободен", "свободен")
    )
    room_status = models.CharField(max_length=20, choices=RoomStatusChoice)
    description = models.TextField()

    def __str__(self):
        return f'{self.hotel}, {self.room_number}'


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_image = models.ImageField(upload_to='room_image/')

    def __str__(self):
        return f'{self.room}'

class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.hotel}, {self.room}'

class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 11)])
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.rating}'



