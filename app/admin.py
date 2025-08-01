from django.contrib import admin
from app.models import User, Room, Reservation

admin.site.register([Room, Reservation])
