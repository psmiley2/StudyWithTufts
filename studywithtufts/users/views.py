from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import UserInfo

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'users/index.html', {'logged_in': False})
    return render(request, "users/index.html", {'logged_in': True})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            UserInfo.objects.create(user=request.user)
            username = form.cleaned_data.get('username')
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


