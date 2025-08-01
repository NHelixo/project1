from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('room_list')
        else:
            messages.error(request,'error')
    else:
        form = UserCreationForm()

    return render(
        request,
        template_name='registration/register.html',
        context = {'form': form}
    )

def auth_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('room_list')
            else:
                messages.error(request, 'Неправильний логін або пароль!')

    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', context = {"form": form})
