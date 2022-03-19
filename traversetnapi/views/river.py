from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from traversetnapi.models import River, river, Member

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
    



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')
        
class RiverMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    
    class Meta:
        model = Member
        fields = ('user', 'about')
    

class RiverSerializer(serializers.ModelSerializer):
    visitors = RiverMemberSerializer(many=True)
    
    class Meta:
        model = River
        fields = ('id', 'title', 'address', 'fish', 'animals', 'about', 'flowchart', 'visitors')
           