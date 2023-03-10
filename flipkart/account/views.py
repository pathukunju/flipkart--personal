from distutils.log import Log
from . import models
from django.shortcuts import redirect, render
from .models import *
from .mixins import MessageHandler
import random
from django.contrib.auth import login, logout, authenticate
from .form import LoginForm
from .models import UserProfile
from django.http import JsonResponse, HttpResponse
from django.urls import reverse
import json

# Create your views here.


def register_view(request):
    form = LoginForm()
    if request.method == 'POST':

        phone_number=request.POST.get('phone_number')
        # form = LoginForm(request.POST)
        
        # phone_number = form.cleaned_data.get("phone")
        user = UserProfile.objects.create(phone=phone_number)
        user.save()
        print('---------')
        return redirect('login')

        # phone_number=request.POST.get('phone_number')
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get("phone")
            user = UserProfile.objects.create(phone=phone_number)
            user.save()
            print('---------')
            return redirect('login')

    return render(request, 'base.html', {'form': form})


def login_view(request):

    if request.method == 'POST':
        try:
            phone_number = request.POST.get('phone_number')
            profile = UserProfile.objects.get(phone=phone_number)
            num_gen = random.randint(1000, 9999)
            profile.otp = num_gen
            profile.save()
            # message_handler=MessageHandler(phone_number,profile.otp)
            # message_handler.send_otp_on_phone()
            print('otp is : ', profile.otp)

            return redirect(f'/account/otp/{profile.uid}')
            # return render(request, 'base.html', {'uid': profile.uid})
        except:
            return redirect('register')
    return render(request, 'base.html')



def otp(request, uid):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = UserProfile.objects.get(uid=uid)
        if otp == profile.otp:
            login(request, profile)
            return redirect('/')
        else:
            return redirect(f'/otp/{uid}')
    else:
        return render(request, 'base.html', {'uid': uid})




def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'POST':
        try:
            phone_number = request.POST.get('phone')
            profile = UserProfile.objects.get(phone=phone_number)
            num_gen = random.randint(1000, 9999)
            profile.otp = num_gen
            print('otp is : ', profile.otp)
            profile.save()
            # message_handler=MessageHandler(phone_number,profile.otp)
            # message_handler.send_otp_on_phone()
            
            # return JsonResponse({'uid':uid})
            # return redirect(f'/account/otp/{profile.uid}')

        except:
            return redirect('register')
    return render(request, 'login.html')
