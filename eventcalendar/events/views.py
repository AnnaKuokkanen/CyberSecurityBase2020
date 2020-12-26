from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Event, Participant

@login_required
def home(request):
    username = request.user.username

    if request.method == "POST" and request.POST['event_name'] != '' and request.POST['event_description'] != '':
        name = request.POST['event_name']
        description = request.POST['event_description']
        new_event = Event(name=name, description=description)
        new_event.save()
        participant = Participant(username=request.user.username)
        participant.save()
        new_event.participants.add(participant)
        new_event.save()
        return HttpResponseRedirect("/home/")

    events = Event.objects.all()
    context = {'username': username, 'events': events}

    return render(request, 'home.html', context)

def query(): 
    return ''