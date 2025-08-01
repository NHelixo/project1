from django.urls import path
from registration import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('authorization/', views.auth_login, name='login')
]
