from rest_framework import serializers
from .models import Event, Participation
from profils.serializers import MemberSerializer

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'status']

class ParticipationSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)
    event = EventSerializer(read_only=True)

    class Meta:
        model = Participation
        fields = ['id', 'member', 'event', 'date_participated', 'attended']
