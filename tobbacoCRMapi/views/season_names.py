from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.season_names import SeasonNames
from ..serializers import SeasonNamesSerializer


class SeasonNamesDetail(APIView):
    """
    get:
    Retrieve a specific season name by id

    put:
    Update a specific season name by id
    """

    def get(self, pk: str) -> Response:
        """
        Get a specific old name.
        """
        seasonName: SeasonNames = SeasonNames.objects.get(pk=pk)
        serilizer: SeasonNamesSerializer = SeasonNamesSerializer(seasonName)
        return Response(serilizer.data)

    @swagger_auto_schema(request_body=SeasonNamesSerializer)
    def put(self, request: Request, pk: str) -> Response:
        """
        Update a specific season name.
        """
        seasonName: SeasonNames = SeasonNames.objects.get(pk=pk)
        serializer: SeasonNamesSerializer = SeasonNamesSerializer(
            seasonName, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk: str) -> Response:
        """
        Delete a specific season name.
        """
        seasonName: SeasonNames = SeasonNames.objects.get(pk=pk)
        seasonName.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SeasonsNamesList(APIView):
    """
    get:
    Retrieve a list of all season names.

    post:
    Create a new season name.
    """

    def get(self) -> Response:
        """
        Retrieve and return all season names.
        """
        seasonNames: SeasonNames = SeasonNames.objects.all()
        serializer: SeasonNamesSerializer = SeasonNamesSerializer(
            seasonNames, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=SeasonNamesSerializer)
    def post(self, request: Request) -> Response:
        """
        Create a new season name.
        """
        serializer: SeasonNamesSerializer = SeasonNamesSerializer(
            data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
