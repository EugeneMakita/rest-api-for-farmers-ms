import base64
import os

from django.conf import settings
from rest_framework.request import Request

from ..helpers.file_helper import FileHelper
from .files_process_service import FilesProcessService


class FileService(FilesProcessService):
    FILE_EXTENSIONS = ["pdf", "doc", "ppt", "docx"]

    @staticmethod
    def store_file(request: Request, base64_data: str) -> dict:
        """Store File

        Args:
            base64_data (str):

        Raises:
            ValueError: if the type of file is not allowed such as video etc

        Returns:
            dict: this contains the url's of the small, medium and large resized images
        """
        ext, base64_content = FileHelper.get_file_string_and_extension(
            base64_data)
        FileService.validate_file_extentions(FileService, ext)
        base_file_name = FileService.create_file_name("doc", ext)
        FileService.save_file_to_disk(base_file_name, base64_content)
        data = {}
        data["path"] = FileService.get_absolute_url(request, base_file_name)
        return data

    @staticmethod
    def save_file_to_disk(base_file_name: str, base64_content: str) -> None:
        """Saves file to disk

        Args:
            base_file_name (str): the name of the file
            base64_content (str): Content of the base64 file
        """
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
        file_name = os.path.join(settings.MEDIA_ROOT, base_file_name)
        with open(file_name, "wb") as f:
            f.write(base64.b64decode(base64_content))

    @staticmethod
    def detete_file() -> bool:
        pass
