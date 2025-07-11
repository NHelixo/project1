from django.shortcuts import render
from app.models import User, Reservation, Room

def room_list_func(request):
    room_list = Room.objects.all()
    context = {"room_list": room_list}
    return render(
        request,
        template_name = 'app/index.html',
        context = context,
    )
