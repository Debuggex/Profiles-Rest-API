from rest_framework.views import APIView
from rest_framework.response import Response



class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request, format=None):

        """Returns a List API View Features"""
        an_apiview=[
            'Uses HTTP methods as functions (get, post, put, patch, delete)',
            'Is similar to traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})