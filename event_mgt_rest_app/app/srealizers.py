from rest_framework import serializers;
from .models import participant,Ticket,Animator,adress,event,Organizer,Reservation
class EventSerialiser(serializers.ModelSerializer):
    class meta:
        model=event
        fields='__all__'
class ticketSerialiser(serializers.ModelSerializer):
    class meta:
        model=Ticket
        fields='__all__'
class participantSerialiser(serializers.ModelSerializer):
    class meta:
        model=participant
        fields='__all__'
class animatorSerialiser(serializers.ModelSerializer):
    class meta:
        model=Animator
        fields='__all__'
class adressSerialiser(serializers.ModelSerializer):
    class meta:
        model=adress
        fields='__all__'
class orginizerSerialiser(serializers.ModelSerializer):
    class meta:
        model=Organizer
        fields='__all__'