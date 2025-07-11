from django.urls import path
import app.views as app_vievs


urlpatterns = [
    path('', app_vievs.room_list_func, name = 'room_list'),
    ]
