from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import RegisterForm
from .models import Profile


def home(request):
    return render(request, "user_management/home.html")


def register(request):
    form = RegisterForm()
    profile = Profile()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, email=email, password=password)
            profile.user = user
            profile.email_address = email
            profile.display_name = form.cleaned_data["display_name"]
            profile.save()
            if user is not None:
                login(request, user)
                return redirect("/")
    return render(request, "registration/register.html", {"form": form})
