from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from traversetnapi.models import River, river

class RiverView(ViewSet):
    
    def list(self, request):
        rivers = River.objects.all()
        serializer = RiverSerializer(rivers, many=True, context={'request': request})
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        
        try:
            river = River.objects.get(pk=pk)
            serializer = RiverSerializer(river, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    
    
    
    
    
    
class RiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = River
        fields = ('id', 'title', 'address', 'fish', 'animals', 'about', 'flowchart', 'visitors')
           