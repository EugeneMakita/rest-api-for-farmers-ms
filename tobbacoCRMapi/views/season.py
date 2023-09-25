from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from ..models.season import Season
from ..serializers.season import SeasonSerializer
from .base import BaseDetailView, BaseListView


class SeasonsDetail(BaseDetailView):
    """
    Season Detail view.

    get:
    Retrieve a specific season by id.

    patch:
    Update a specific season by id.

    delete:
    Delete a specific seaon by id.
    """
    model = Season
    serializer_class = SeasonSerializer

    @swagger_auto_schema(request_body=SeasonSerializer)
    def patch(self, request, pk: str) -> Response:
        return super().patch(request, pk)


class SeasonsList(BaseListView):
    """
    Season Detail view.

    get:
    Retrieve all seasons.

    post:
    Create a new season.
    """
    model = Season
    serializer_class = SeasonSerializer

    @swagger_auto_schema(request_body=SeasonSerializer)
    def post(self, request) -> Response:
        return super().post(request)
