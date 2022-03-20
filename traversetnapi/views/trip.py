from django.core.exceptions import ValidationError
from rest_framework import status
from django.contrib.auth.models import User
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from traversetnapi.models import Trip, River, Place, Member

class TripView(ViewSet):
    
    def create(self, request):
        
        
        member = Member.objects.get(user=request.auth.user)
        river = River.objects.get(pk=request.data["river"])
        place = Place.objects.get(pk=request.data["place"])
        
        
        trip = Trip()
        trip.title = request.data["title"]
        trip.river = river
        trip.place = place
        trip.date = request.data["date"]
        trip.member = member
        river.visitors.add(member)
        river.save()
        place.visitors.add(member)
        place.save()
        
        try: 
            trip.save()
            serializer = TripSerializer(trip, context={'request': request})
            return Response(serializer.data)
        
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        try:
            trip = Trip.objects.get(pk=pk)
            serializer = TripSerializer(trip, context={'request': request})
            return Response(serializer.data)
        except Exception as ex: 
            return HttpResponseServerError(ex)
        
    def update(self, request, pk=None):
        
        river = River.objects.get(pk=request.data["river"])
        place = Place.objects.get(pk=request.data["place"])
        member = Member.objects.get(user=request.auth.user)
        
        trip = Trip.objects.get(pk=pk)
        trip.title = request.data["title"]
        trip.river = river
        trip.place = place
        trip.date = request.data["date"]
        trip.member = member
        trip.save()
        
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk=None):
        try:
            trip = Trip.objects.get(pk=pk)
            trip.delete()
            
            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Trip.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def list (self, request):
        trips = Trip.objects.all()
        
        river = self.request.query_params.get('type', None)
        if river is not None:
            trips = trips.filter(river_id=river)
            
        place = self.request.query_params.get('type', None)
        if place is not None:
            trips = trips.filter(place_id=place)
        
        member_token = self.request.query_params.get('member', None)
        
        if member_token is not None:
            member = Member.objects.get(user = User.objects.get(auth_token=member_token))
            
            trips = Trip.objects.filter(user=member)
            
        serializer = TripSerializer(
            trips, many= True, context={'request': request})
        return Response(serializer.data)       
        
        
        
        
class TripMemberSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Member
        fields = ['user', 'about']
        
class TripRiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = River
        fields = ['id', 'title', 'address', 'fish', 'animals', 'about', 'flowchart', 'visitors']
        
class TripPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id','address', 'wildlife', 'about', 'visitors']
        
class TripSerializer(serializers.ModelSerializer):
    member = TripMemberSerializer(many=False)
    river = TripRiverSerializer(many=False)
    place = TripPlaceSerializer(many=False)
    
    class Meta:
        model = Trip
        fields = ('id', 'title', 'river', 'place', 'date', 'member')
        
        
        