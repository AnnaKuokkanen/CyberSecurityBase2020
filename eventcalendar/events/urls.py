from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('event/<int:eventid>', views.event, name='event')
]