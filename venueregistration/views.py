from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from venueregistration.models import Location, VenueType, EventType, Venue
from venueregistration.serializers import ManagerSerializer, LocationSerializer, VenueTypeSerializer, \
    EventTypeSerializer, VenueSerializer


class ManagerList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = ManagerSerializer(users, many=True)
        return Response(serializer.data)


class LocationList(APIView):
    def get(self, request, format=None):
        location = Location.objects.all()
        serializer = LocationSerializer(location, many=True)
        return Response(serializer.data)


class VenueTypeList(APIView):
    def get(self, request, format=None):
        users = VenueType.objects.all()
        serializer = VenueTypeSerializer(users, many=True)
        return Response(serializer.data)


class EventTypeList(APIView):
    def get(self, request, format=None):
        users = EventType.objects.all()
        serializer = EventTypeSerializer(users, many=True)
        return Response(serializer.data)



class VenueList(APIView):
    def get(self, request, format=None):
        users = Venue.objects.all()
        serializer = VenueSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VenueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)