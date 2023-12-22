from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """returns a list of APIView features"""
        an_apiview=[
        'Uses HTTP methods as function (get,post,patch,put,delete)',
        'Is similar to a traditional Django view',
        'is mapped manually to URLs',
        ]

        return Response({'message':'Hello!','an_apiview': an_apiview})
         
