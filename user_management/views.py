from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import RegisterForm, UpdateForm
from .models import Profile


def home(request):
    return render(request, "user_management/home.html")

def user_profile(request):
    user = request.user.profile
    return render(request, "user_management/profile.html", {"profile" : user})

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


def update_profile(request):
    profile = request.user.profile
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("user_management:profile")
    else:
        form = UpdateForm(instance=profile)
    return render(request, "user_management/profile_update.html", {"form": form})