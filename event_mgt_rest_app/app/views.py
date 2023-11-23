from django.shortcuts import render
from rest_framework import viewsets
from .models import participant,Ticket,Animator,adress,event,Organizer,Reservation
from .srealizers import EventSerialiser,participantSerialiser
# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset=event.objects.all()
    serializer_class=EventSerialiser
class ParticipantViewSet(viewsets.ModelViewSet):
    queryset=participant.objects.all()
    serializer_class=participantSerialiser
    http_method_names=['GET','PUT','DELETE']
