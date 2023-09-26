from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from ..models.images import Images
from ..serializers.images import ImagesSerializer
from ..services.image_service import ImageService
from .files_base import FilesBaseDetailView, FilesBaseListView


class ImageDetailView(FilesBaseDetailView):
    """
    Images Detail view.

    get:
    Retrieve a specific images by id.

    delete:
    Delete a specific images by id.
    """

    model = Images
    serializer_class = ImagesSerializer


class ImagesList(FilesBaseListView):
    """
    Images List view.

    get:
    Retrieve a list of all Images.

    post:
    Create a new Image.
    """

    model = Images
    serializer_class = ImagesSerializer
    file_service_class = ImageService

    @swagger_auto_schema(request_body=ImagesSerializer)
    def post(self, request) -> Response:
        return super().post(request)
