from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.db import connection
from .models import Event, Participant

@login_required
def home(request):
	username = request.user.username
	events = Event.objects.all()

	if request.method == "POST" and request.POST['event_name'] != '' and request.POST['event_description'] != '':
		name = request.POST['event_name']
		description = request.POST['event_description']
		new_event = Event(name=name, description=description)
		new_event.save()
		obcj, participant = Participant.objects.get_or_create(username=request.user.username)
		new_event.participants.add(participant)
		new_event.save()
		return HttpResponseRedirect("/home/")

	if request.method == "GET" and 'event_search' in request.GET:
		#print('Searching... ' + str(query(request.GET['event_search'])))
		events = query(request.GET['event_search'])

	context = {'username': username, 'events': events}

	#print('events are' + str(events)) 

	return render(request, 'home.html', context)

def query(search):
	print('Searching with keyword ' + search) 
	# with connection.cursor() as cursor:
	# 	response = cursor.execute("SELECT * FROM events_event WHERE name LIKE '%%%s%%'" % (search)).fetchall()
	# 	for r in response:
	# 		print('Match ' + str(r))
	response = Event.objects.raw("SELECT * FROM events_event WHERE name LIKE '%%%s%%'" % (search))
	for r in response: 
		print('Match ' + str(r))
	return response


def event(request, id):
	return None