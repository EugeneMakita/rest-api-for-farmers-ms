from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..models import SeasonNames
from ..serializers import SeasonNamesSerializer

class SeasonNamesDetail(APIView):
    """
    get:
    Retrieve a specific season name by id
    
    put:
    Update a specific season name by id
    """

    def get(self, request, pk):
        """
        Get a specific old name.
        """
        seasonName = SeasonNames.objects.get(pk=pk)
        serilizer = SeasonNamesSerializer(seasonName)
        return Response(serilizer.data)

    @swagger_auto_schema(request_body=SeasonNamesSerializer)
    def put(self, request, pk):
        """
        Update a specific season name.
        """
        seasonName = SeasonNames.objects.get(pk=pk)
        serializer = SeasonNamesSerializer(seasonName, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a specific season name.
        """
        seasonName = SeasonNames.objects.get(pk=pk)
        seasonName.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SeasonsNamesList(APIView):
    """
    get:
    Retrieve a list of all season names.
    
    post:
    Create a new season name.
    """

    def get(self, request):
        """
        Retrieve and return all season names.
        """
        seasonNames = SeasonNames.objects.all()
        serializer = SeasonNamesSerializer(seasonNames, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=SeasonNamesSerializer)
    def post(self, request):
        """
        Create a new season name.
        """
        serializer = SeasonNamesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)