from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
# from django.contrib.auth.decorators import login_required
from django.db import connection
from .models import Event, Participant

# @login_required
def home(request):
	username = request.user.username
	if username != '':
		current_user = Participant.objects.get(username=username)
		events = Event.objects.all().filter(participants=current_user)
	else:
		events = Event.objects.all()

	if request.method == "POST" and request.POST['event_name'] != '' and request.POST['event_description'] != '':
		name = request.POST['event_name']
		description = request.POST['event_description']
		new_event = Event(name=name, description=description)
		new_event.save()
		obj, participant = Participant.objects.get_or_create(username=request.user.username)

		if participant == True:
			new_event.participants.add(participant)
		else: 
			new_event.participants.add(obj)

		new_event.save()
		return HttpResponseRedirect("/home/")

	if request.method == "GET" and 'event_search' in request.GET:
		events = query(request.GET['event_search'])

	context = {'username': username, 'events': events}

	return render(request, 'home.html', context)

def query(search):
	response = Event.objects.raw("SELECT * FROM events_event WHERE name LIKE '%%%s%%'" % (search))
	return response


def event(request, id):
	event = Event.objects.get(id=id)
	
	context = {'event': event}

	return render(request, 'event.html', context)