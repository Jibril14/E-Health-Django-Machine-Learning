from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import auth


def register(request):

    if request.method == "POST":
        form = UserRegistrationForm()
        try:
            first_name = request.POST.get("first_name", "")
            last_name = request.POST.get("last_name", "")
            email = request.POST.get("email", "")
            username = request.POST.get("username", "")
            address = request.POST.get("address", "")
            role = request.POST.get("role", "")
            password = request.POST.get("password", "")
            user = User(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                address=address,
                role=role,
                password=password)
            user.save()
            return HttpResponseRedirect(reverse('login'))

        except Exception as error:
            form = UserRegistrationForm()
            context = {
                "form": form,
                "error": error,
            }
            return render(request, "account/register.html", context)

    else:
        form = UserRegistrationForm()
    context = {
        "form": form
    }
    return render(request, "account/register.html", context)


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            return render(request, "account/login.html",
                          {"error": "Invalid Credential"})

    return render(request, "account/login.html")


@login_required
def logout(request):
    auth.logout(request)
    return redirect("home")


@login_required
def profile(request):
    user = User.objects.all()

    current_user = request.user
    print("curr", current_user)

    user = user.filter(email=current_user)
    return render(request, "account/profile.html", {"user": user})

# prediction = prediction.filter(user=user)


def doctors(request):
    return render(request, "account/doctors.html")
