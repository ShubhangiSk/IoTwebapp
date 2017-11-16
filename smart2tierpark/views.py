from django.shortcuts import render
from .forms import SignUpForm
from .Platform import Platform
from .models import Log
from .Bill import Bill
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
import urllib3
import json
import time

flag=0
platform= None
# Create your views here.
def home_page(request):
    return render(request, 'smart2tierpark/home_page.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home_page')
    else:
        form = SignUpForm()
    return render(request, 'smart2tierpark/sign_up.html', {'form': form})


def park(request):
    if request.user.is_authenticated():
        flag=1
        global platform
        platform=Platform()
        return render(request, 'smart2tierpark/park.html',{'platform':platform})
    else:
        return redirect('home_page')

def unpark(request):
    if request.user.is_authenticated():
        global platform
        bill=Bill(platform)
        Log.objects.create(veh_num=request.user,platform_number=bill.pnum,timein=bill.start_time,timeout=bill.endtime,totaltime=bill.totaltime,totalcost=bill.totalcost)
        return render(request, 'smart2tierpark/unpark.html',{'bill':bill})
    else:
        return redirect('home_page')

