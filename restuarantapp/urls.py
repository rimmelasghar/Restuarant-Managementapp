from django.urls import path
from . import views
urlpatterns = [
    path('',views.home2,name='home'),
    path('reservation/<int:tablepk>/<int:bookpk>/',views.reservation,name = 'reservation'),
    path('myreservations/',views.myreservation,name = 'myreservation')
]
