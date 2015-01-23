from django.contrib.auth.models import User
from rest_framework import serializers
from venueregistration.models import Location, VenueType, EventType, Venue

__author__ = 'prasanna'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')



class LocationSerializer(serializers.ModelSerializer):
    id= serializers.IntegerField()
    name = serializers.SerializerMethodField('fetch_name')

    def fetch_name(self, obj):
        return obj.name + ", " + obj.city.name

    class Meta:
        model = Location
        fields = ('id', 'name')



class VenueTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenueType
        fields = ('id', 'name')



class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ('id', 'name')


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model=Venue


