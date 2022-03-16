from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from traversetnapi.models import Favorite
from traversetnapi.models import River, Place, Member

class FavoriteView(ViewSet):
    
    def list(self, request):
        favorites = Favorite.objects.all()
        serializer = FavoriteSerializer(favorites, many=True, context={'request': request})
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        
        try:
            favorite = Favorite.objects.get(pk=pk)
            serializer = FavoriteSerializer(favorite, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
        
        
    def create(self, request, pk=None):
        
        user = request.auth.user.member
        
        river = River.objects.get(pk=request.data["riverId"])
        place = Place.objects.get(pk=request.data["placeId"])
        
        
        favorite = Favorite()
        favorite.riverId = river
        favorite.placeId = place
        favorite.memberId = user
        
        try:
            favorite.save()
            serializer = FavoriteSerializer(favorite, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        try:
            favorite = Favorite.objects.get(pk=pk)
            favorite.delete()
            
            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Favorite.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'riverId', 'placeId', 'memberId')