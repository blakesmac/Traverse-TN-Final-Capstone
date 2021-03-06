from django.contrib.auth.models import User
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from traversetnapi.models import Member, trip, Trip

class MemberView(ViewSet):
    
    def list(self, request):
        
        member = Member.objects.get(user=request.auth.user)
        
        member = MemberSerializer(
            member, many=False, context ={'request': request}
        )
        
        trip = self.request.query_params.get('type', None)
        if trip is not None: 
            member = member.filter(trip_id=trip)
        
        
        profile = {}
        profile["member"] = member.data
        return Response(profile)
    
    def retrieve(self, request, pk=None):
        
        try:
            
            member = Member.objects.get(pk=pk)
            serializer = MemberSerializer(member, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
        
class MemberTripSerializer(serializers.ModelSerializer):
    class Meta:
        model: Trip 
        fields = ('id', 'title', 'river', 'place', 'date', 'member')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')
        
class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    
    class Meta:
        model = Member
        fields = ('user', 'about')