from msilib.schema import tables
from unicodedata import name
from django.shortcuts import render, get_object_or_404 , redirect
from restuarantapp.models import Table,Booking
from .forms import SearchReservation
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q   
# Create your views here.


def home2(request):
    if request.method == 'GET':
        table = Table.objects.all()
        return render(request, 'home.html',{'tables':table})
    if request.method == 'POST':
        form = SearchReservation(request.POST)
        if form.is_valid():
            reservationField = form.cleaned_data.get("reservationField")
            capacity = form.cleaned_data.get("capacity")
            dumm_table = Table.objects.get(id = 1)
            booking = Booking.objects.create(
                user = request.user,
                capacity = capacity,
                reservationField = reservationField,
                table = dumm_table,
            )
            bookings = Booking.objects.filter(reservationField = reservationField)
            table_lst = [i.table.id for i in bookings]
            table = Table.objects.filter(capacity__gte=capacity).exclude(id__in = table_lst)
            booking.save()
        return render(request,'home.html',{'tables':table,'bookid':booking.id})

def reservation(request,tablepk,bookpk):
    table = get_object_or_404(Table,pk=tablepk)
    booking = get_object_or_404(Booking,id = bookpk)
    booking.table = table
    booking.save()
    reservations = Booking.objects.filter(user = request.user)
    return render(request,'reservations.html',{'reservations':reservations})

def myreservation(request):
        reservations = Booking.objects.filter(user = request.user)
        if len(reservations) == 0:
            reservations = 0
        return render(request,'reservations.html',{'reservations':reservations})