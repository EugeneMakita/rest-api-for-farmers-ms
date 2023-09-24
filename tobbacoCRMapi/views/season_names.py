from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from ..models.season_names import SeasonNames
from ..serializers.season_names import SeasonNamesSerializer
from .base import BaseDetailView, BaseListView


class SeasonNamesDetail(BaseDetailView):
    """
    Season Names Detail view.

    get:
    Retrieve a specific name by id.

    put:
    Update a specific name by id.

    delete:
    Delete a specific name by id.
    """
    model = SeasonNames
    serializer_class = SeasonNamesSerializer

    @swagger_auto_schema(request_body=SeasonNamesSerializer)
    def patch(self, request, pk: str) -> Response:
        return super().patch(request, pk)


class SeasonsNamesList(BaseListView):
    """
    Season Names Detail view.

    get:
    Retrieve all names.

    post:
    Create a new name.
    """
    model = SeasonNames
    serializer_class = SeasonNamesSerializer

    @swagger_auto_schema(request_body=SeasonNamesSerializer)
    def post(self, request, pk: str) -> Response:
        return super().post(request, pk)
