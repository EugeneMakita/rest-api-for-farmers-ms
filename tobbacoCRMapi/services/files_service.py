import base64
import os

from django.conf import settings
from django.utils.crypto import get_random_string

from ..helpers.file_helper import FileHelper
from .files_process_service import FilesProcessService


class FileService(FilesProcessService):
    @staticmethod
    def store_file(request, base64_data: str) -> dict:
        """Store File

        Args:
            base64_data (str):

        Raises:
            ValueError: if the type of file is not allowed such as video etc

        Returns:
            tuple: this contains the url's of the small, medium and large resized images
        """
        ext, base64_content = FileHelper.get_file_string_and_extension(
            base64_data)
        FileService.validate_file_extentions(ext)
        base_file_name = FileService.create_file_name(ext)
        FileService.save_file_to_disk(base_file_name, base64_content)
        return FileService.get_file_object(request, base_file_name)

    @staticmethod
    def validate_file_extentions(ext: str):
        """This checks if the file uploaded is the correct one

        Args:
            ext (str): The extention of the uploded file

        Raises:
            ValueError: This is raised when the file uploaded is the wrong ext
        """
        if ext not in ["pdf", "doc", "ppt", "docx"]:
            raise ValueError("File should be a pdf, doc, docx, ppt")

    @staticmethod
    def create_file_name(ext: str) -> str:
        """Create new file name

        Args:
            ext (str): the extention of the file

        Returns:
            str: the newly created file name
        """
        return f"media_doc_{get_random_string(16)}.{ext}"

    @staticmethod
    def get_file_object(request, base_file_name: str) -> tuple:
        """Creates A tuple to use in creating a File Object

        Args:
            request (_type_): This is used to get the full url of the file
            base_file_name (str): the name of the file

        Returns:
            tuple: This is the tuple used to create File Object
        """
        relative_url = settings.MEDIA_URL + base_file_name
        absolute_url = request.build_absolute_uri(relative_url)

        data = {}
        data["path"] = absolute_url
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
