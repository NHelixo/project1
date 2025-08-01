from django.shortcuts import render, get_object_or_404, redirect
from app.models import Reservation, Room
from datetime import datetime
import calendar
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User

def room_list_func(request):
    room_list = Room.objects.all()
    context = {"room_list": room_list}
    return render(
        request,
        template_name = 'app/index.html',
        context = context,
    )

def room_detail(request, num_room):
    room = Room.objects.get(num_room=num_room)
    year = datetime.now().year
    month = datetime.now().month

    cal = calendar.HTMLCalendar(calendar.MONDAY)
    calendar_html = cal.formatmonth(year, month)
    context = { "room": room,
                'calendar': calendar_html,
                'month': month,
                'year': year
                }
    return render(
        request,
        template_name = 'app/room_info.html',
        context = context,
    )

def reservation(request, num_room):
    room = get_object_or_404(Room, num_room=num_room)
    if request.method == "POST":
        if request.user.is_authenticated:
            print("Викликано reservation view")
            username = request.user.username
            user = User.objects.get(username=username)
            date_start = request.POST.get("date_start")
            date_end = request.POST.get("date_end")
            if date_end > date_start:
                if Reservation.objects.filter(room=room, date_start__lt=date_end, date_end__gt=date_start).exists():
                    return redirect('room_detail', num_room=num_room)
                if not room.booking_status:
                    room.booking_status = True
                    room.save()
                Reservation(user=user,
                            room=room,
                            date_start=date_start,
                            date_end=date_end).save()

                return redirect('room_detail', num_room=num_room)
            else:
                return redirect('room_detail', num_room=num_room)
        else:
            return redirect('login')

    else:
        context = {"room": room}
        return render(request, 'app/product_info.html', context)

def hat(request):
    return render(request, 'app/hat.html')

def logout_view(request):
    logout(request)
    return redirect('room_list')
