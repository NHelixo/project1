from django.db import models

class User(models.Model):
    login = models.CharField(max_length=200, unique=True, null=False)
    password = models.CharField(max_length=128, null=False)
    phone = models.IntegerField(null=False, unique=True)

    def __str__(self):
        return self.login
    

class Room(models.Model):
    num_room = models.IntegerField(unique=True, null=False)
    num_beds = models.IntegerField(null=False)
    room_class = models.CharField(null=False, max_length=20)
    price = models.FloatField(null=False)
    def __str__(self):
        return f"Номер: {self.num_room}, Клас: {self.room_class}"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=False)
    date_start = models.DateField(null=False)
    date_end = models.DateField(null=False)
    def __str__(self):
        return f"Користувач: {self.user.login}, Кімната: {self.room.num_room}"
