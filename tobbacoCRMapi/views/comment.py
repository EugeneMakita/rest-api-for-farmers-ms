from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from ..models.comments import Comments
from ..serializers.comments import CommentsSerializer
from .base import BaseDetailView, BaseListView


class CommentsDetail(BaseDetailView):
    """
    Comment Detail view.

    get:
    Retrieve a specific contact by id.

    patch:
    Update a specific contact by id.

    delete:
    Delete a specific contact by id.
    """

    model = Comments
    serializer_class = CommentsSerializer

    @swagger_auto_schema(request_body=CommentsSerializer)
    def patch(self, request, pk: str) -> Response:
        return super().patch(request, pk)


class CommentsList(BaseListView):
    """
    Comment List view.

    get:
    Retrieve a list of all contacts.

    post:
    Create a new contact.
    """

    model = Comments
    serializer_class = CommentsSerializer

    @swagger_auto_schema(request_body=CommentsSerializer)
    def post(self, request) -> Response:
        return super().post(request)
