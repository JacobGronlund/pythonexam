from django.shortcuts import render, HttpResponse, redirect
from models import *
import time
import datetime
from django.contrib import messages
import bcrypt


# Create your views here.
def index(request):
    return render(request, 'exam/index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags = tag)
        return redirect(index)
    else:
        count = User.objects.filter(username = request.POST['username']).count()
        if count > 0:
            messages.error(request, 'username already used')
        else:
            hashedpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            User.objects.create(name = request.POST['name'], username = request.POST['username'], password = hashedpw, created_at=datetime.datetime.now())
        return redirect(index)
    
def login(request):
    user = User.objects.get(username = request.POST['login_username'])
    if bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode()):
        request.session['userid'] = user.id
        print request.session['userid']
        return redirect(dashboard)
    messages.error(request, 'incorrect password')
    return redirect(index)

def add(request):

    return render(request, 'exam/add.html')

def addtrip(request):
    a_user = User.objects.get(id = request.session['userid'])
    a_trip = Trip.objects.create(destination = request.POST['destination'], desc = request.POST['desc'], datefrom = request.POST['datefrom'], dateto = request.POST['dateto'])
    errors = Trip.objects.trip_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect(add)
    a_user.planned_trips.add(a_trip)
    return redirect(dashboard)
def dashboard(request):
    
    content = {
        'a_user': User.objects.get(id = request.session['userid']),
        'users': User.objects.exclude(id = request.session['userid']),
        'trips': Trip.objects.all()
    }
    return render(request, 'exam/dashboard.html', content)

def tripdetails(request, tripid):
    user = User.objects.all()
    owner = Trip.objects.get(id=tripid).users.first()
    tripusers = Trip.objects.get(id=tripid).users.exclude(id = owner.id)
    a_trip = Trip.objects.get(id = tripid)
    print tripusers
    content = {
        'owner': owner,
        'trip': a_trip,
        'tripusers': tripusers
    }
    return render(request,'exam/destination.html', content)
def join(request, tripid):
    a_user = User.objects.get(id = request.session['userid'])
    a_trip = Trip.objects.get(id = tripid)
    a_user.planned_trips.add(a_trip)
    return redirect(dashboard)
#username George
#pass 1234567890