from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from ..models.files import Files
from ..serializers.files import FilesSerializer
from ..services.files_service import FileService
from .files_base import FilesBaseDetailView, FilesBaseListView


class FilesDetailView(FilesBaseDetailView):
    """
    Files Detail view.

    get:
    Retrieve a specific file by id.

    delete:
    Delete a specific file by id.
    """

    model = Files
    serializer_class = FilesSerializer


class FilesList(FilesBaseListView):
    """
    Files List view.

    get:
    Retrieve a list of all files.

    post:
    Create a new files.
    """

    model = Files
    serializer_class = FilesSerializer
    file_service_class = FileService

    @swagger_auto_schema(request_body=FilesSerializer)
    def post(self, request) -> Response:
        return super().post(request)
