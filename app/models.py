from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    num_room = models.IntegerField(unique=True, null=False)
    num_beds = models.IntegerField(null=False)
    room_class = models.CharField(null=False, max_length=20)
    price = models.FloatField(null=False)
    booking_status = models.BooleanField(null=False)
    def __str__(self):
        return f"Номер: {self.num_room}, Клас: {self.room_class}"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=False)
    date_start = models.DateField(null=False)
    date_end = models.DateField(null=False)
    def __str__(self):
        return f"Користувач: {self.user.username}, Кімната: {self.room.num_room}"
