# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from .models import User, Book, Review
from ..reglogin.models import User
from .models import Trip
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
def dashboard(request):
    try:
        request.session['user_id']
    except:
        return redirect('/')
    request.session['user_id']
    context ={
        'user': User.objects.get(id=request.session['user_id']),
        'trips': Trip.objects.all().exclude(travelers_id=request.session['user_id'])
    }
    return render(request, 'travel/dashboard.html', context)

def addtrip(request):
    return render(request,'travel/travelform.html')

def processtrip(request):
    user_id = request.session['user_id']
    result = Trip.objects.validate_trip(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/addtrip')
    Trip.objects.create(
        destination=request.POST['destination'],
        description=request.POST['description'],
        trip_start=request.POST['trip_start'],
        trip_end=request.POST['trip_end'],
        travelers=User.objects.get(id=request.session['user_id'])
    )
    return redirect('/travels')

def showtrip(request, trip_id):
    context = {
        'trip': Trip.objects.get(id=trip_id),
        'users': User.objects.all(),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'travel/trip.html', context)

def deletetrip(request, trip_id):
    trip = Trip.objects.get(id=trip_id).delete()
    return redirect('/travels')

def jointrip(request, trip_id):
    context = {
        'trip': Trip.objects.get(id=trip_id),
        'users': User.objects.all(),
        'user': User.objects.get(id=request.session['user_id'])
    }
    trip_to_add = Trip.objects.get(id=trip_id)
    trip_to_add.travelers = User.objects.get(id=request.session['user_id'])
    trip_to_add.save()
    return render(request, 'travel/trip.html', context)