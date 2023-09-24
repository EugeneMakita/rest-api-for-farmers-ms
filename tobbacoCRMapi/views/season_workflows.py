from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from ..models.season_workflows import SeasonWorkflows
from ..serializers.season_workflows import SeasonWorkflowsSerializer
from .base import BaseDetailView, BaseListView


class SeasonWorkflowsDetail(BaseDetailView):
    """
    Season Worfkflows Detail view.

    get:
    Retrieve a specific workflow by id.

    put:
    Update a specific workflow by id.

    delete:
    Delete a specific workflow by id.
    """
    model = SeasonWorkflows
    serializer_class = SeasonWorkflowsSerializer

    @swagger_auto_schema(request_body=SeasonWorkflowsSerializer)
    def patch(self, request, pk: str) -> Response:
        return super().patch(request, pk)


class SeasonWorkflowList(BaseListView):
    """
    Season Workflows Detail view.

    get:
    Retrieve all workflows.

    post:
    Create a new Workflow.
    """
    model = SeasonWorkflows
    serializer_class = SeasonWorkflowsSerializer

    @swagger_auto_schema(request_body=SeasonWorkflowsSerializer)
    def post(self, request, pk: str) -> Response:
        return super().post(request, pk)
