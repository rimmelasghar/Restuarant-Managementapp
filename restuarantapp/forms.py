from dataclasses import fields
from django import forms
from .models import Table,Booking

class SearchReservation(forms.ModelForm):
    reservationField = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    capacity = forms.IntegerField(min_value=0)

    class Meta:
        model = Booking
        fields = ['reservationField','capacity']
        

