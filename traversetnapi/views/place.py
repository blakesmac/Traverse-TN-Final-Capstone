from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from traversetnapi.models import Place, place, Member

class PlaceView(ViewSet):
    
    def list(self, request):
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True, context={'request': request})
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        
        try:
            place = Place.objects.get(pk=pk)
            serializer = PlaceSerializer(place, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')
        
class PlaceMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    
    class Meta:
        model = Member
        fields = ('user', 'about')
        
class PlaceSerializer(serializers.ModelSerializer):
    visitors = PlaceMemberSerializer(many=True)
    class Meta:
        model = Place
        fields = ('id', 'address', 'wildlife', 'about', 'visitors')
    