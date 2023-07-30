from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def homepage(request):

    return render(request=request, template_name="homepage.html")


def Register(request):

    uname = request.POST.get("uname")
    pwd = request.POST.get("pass1")
    repwd = request.POST.get("pass2")
    email = request.POST.get("email")
    Ph_No = request.POST.get("phonenum")

    if User.objects.filter(username=uname):
        messages.error(request=request, message="User already exists")
        return redirect('register')

    if len(Ph_no) != 10:
        messages.error(request=request,
                       message="Please enter 10 digit mobile number !")
        return redirect('register')

    if pwd != repwd:
        messages.error(request=request, message="Password Does not Match !")
        return redirect('register')

    if request.method == "POST":

        user = User.objects.create_user(
            username=uname, email=email, password=pwd)
        user.save()
        messages.success(
            request=request, message="Account created Successfully !")
        return redirect('signin')

    return render(request=request, template_name="Register.html")


def Signin(request):

    uname = request.POST.get("uname")
    pwd = request.POST.get("pass")

    user = authenticate(request=request, username=uname, password=pwd)

    if request.method == "POST":
        if user is not None:

            login(request=request, user=user)
            return redirect('home')

        else:
            messages.error(request=request,
                           message="Username or password is Incorrect")
            return redirect("signin")

    return render(request=request, template_name="signin.html")


def coverpage(request):

    return render(request=request, template_name="coverpage.html")


def Log_out(request):
    logout(request=request)

    return redirect("coverpage")
