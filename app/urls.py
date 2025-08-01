from django.urls import path
import app.views as app_vievs


urlpatterns = [
    path('', app_vievs.room_list_func, name = 'room_list'),
    path('<int:num_room>/', app_vievs.room_detail, name = 'room_detail'),
    path('reserve/<int:num_room>/', app_vievs.reservation, name = 'reservation'),
    path('', app_vievs.hat, name = 'auth'),
    path('logout', app_vievs.logout_view, name = 'logout'),
    ]
