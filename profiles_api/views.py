from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 

from profiles_api import Serializer



class HelloAPIView(APIView):
    """Test API View"""

    serializer_class=Serializer.HelloSerializer

    def get(self, request, format=None):

        """Returns a List API View Features"""
        an_apiview=[
            'Uses HTTP methods as functions (get, post, put, patch, delete)',
            'Is similar to traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self, request):
        """Create a Hello message with our name"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message= f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors
            , status=status.HTTP_400_BAD_REQUEST)  

    def put(self, request,pk=None):
        """Handle Updating Object"""
        return Response({'method':'PUT'})
    
    def patch(self, request,pk=None):
        """Handle Partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an Object"""
        return Response({'method':'DELETE'})