from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from traversetnapi.models import Place, place

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
        
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'address', 'wildlife', 'about', 'visitors')
    