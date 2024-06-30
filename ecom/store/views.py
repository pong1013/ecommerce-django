from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib import messages

# For login
from django.contrib.auth import authenticate, login, logout

# For register
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


def home(request):
    products = Product.objects.all()
    return render(request, "navbar/home.html", {"products": products})


def about(request):
    return render(request, "navbar/about.html", {})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, ("Welcome back! You've logged in successfully."))
            return redirect("home")
        else:
            messages.success(
                request,
                (
                    "Login failed. Please check your username and password and try again."
                ),
            )
            return redirect("login")
    return render(request, "accounts/login.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You've been logged out. See you next time!"))
    return redirect("home")


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Welcome! You have registered successfully!"))
            return redirect("home")
        else:
            messages.success(
                request, ("Whoops! There is a problem registering, please try again...")
            )
            return redirect("register")

    else:
        return render(request, "accounts/register.html", {"form": form})


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "product.html", {"product": product})


def category(request, foo):
    # Replace - to spaces
    foo = foo.replace("-", " ")
    # Grab the category from the url
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(
            request,
            "navbar/category.html",
            {"products": products, "category": category},
        )
    except:
        messages.success(request, ("The category doesn't exist"))
        return redirect("home")


def category_summary(request):
    categories = Category.objects.all()

    return render(request, "navbar/category_summary.html", {"categories": categories})
