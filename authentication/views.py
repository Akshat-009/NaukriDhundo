from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Verification
from helpers import send_mail
# Create your views here.

def link_generator(user,email):
    Verification(user_id=user.id).save()
    try:
        verified = Verification.objects.get(user_id=user.id)
    except Verification.MultipleObjectsReturned:
        verified = Verification.objects.filter(user_id=user.id)
        verified=verified[len(verified)-1]
    
    send_mail(email,"Verify your email",f"Click here <a href='http://127.0.0.1:8000/auth/verify/{verified.code}'>To Verify Account</a>")

def register(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        User.objects.create_user(email=email,username=email,password=password)
        user = User.objects.get(username=email)
        Verification(user_id=user.id).save()
        verified = Verification.objects.get(user_id=user.id)
        send_mail(email,"Verify your email",f"Click here <a href='http://127.0.0.1:8000/auth/verify/{verified.code}'>To Verify Account</a>")
        return render(request,"authentication/registered.html")
    else:
        return render(request,"authentication/register.html")




def login_view(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]

        user=authenticate(username=email,password=password)
        if user is not None :
            try :
                Verification.objects.get(user_id=user.id)
                return render(request,"authentication/invalid.html",
                {
                    "message":"Complete Email Verification First, Click to  <a href='/auth/verify/new'>Send Verification link again </a> "
                }) 
            except Verification.DoesNotExist:
                login(request,user)
                return HttpResponseRedirect("/")

        else:
            return render(request,"authentication/invalid.html",{
                "message":"Invalid Credentials"
            })
    else:
        return render(request,"authentication/login.html")
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


def verify(request,verification_code):
    try:
        user_id=Verification.objects.get(code=verification_code).user_id
        Verification.objects.get(code=verification_code).delete()
        Verification.objects.filter(user_id=user_id).delete()
        return HttpResponseRedirect("auth/login")
    except Verification.DoesNotExist:
        return render(request,"authentication/invalid.html",{
            "message":"Invalid Code"
        })

def verify_again(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST["email"])
            link_generator(user,request.POST["email"])
        except User.DoesNotExist:
            return render(request,"authentication/success.html",{
                "message":"Link sent to email id"
            })
    else:
        return render(request,"authentication/verify_again.html")