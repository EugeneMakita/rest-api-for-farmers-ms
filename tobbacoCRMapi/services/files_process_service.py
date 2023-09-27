from abc import ABC, abstractmethod

from django.conf import settings
from django.utils.crypto import get_random_string
from rest_framework.request import Request


class FilesProcessService(ABC):
    LENGTH_OF_FILE_NAME = 16
    FILE_EXTENSIONS = []

    @staticmethod
    def validate_file_extentions(cls, ext: str):
        """This checks if the file uploaded is the correct one

        Args:
            ext (str): The extention of the uploded file

        Raises:
            ValueError: This is raised when the file uploaded is the wrong ext
        """
        if ext not in cls.FILE_EXTENSIONS:
            file_extensions = ", ".join(cls.FILE_EXTENSIONS)
            raise ValueError(
                f"File {ext} is not suppoerted try {file_extensions}")

    @staticmethod
    def get_absolute_url(request: Request, base_file_name: str) -> str:
        """_summary_

        Args:
            request (_type_): _description_
            base_file_name (_type_): _description_

        Returns:
            str: _description_
        """
        relative_url = settings.MEDIA_URL + base_file_name
        return request.build_absolute_uri(relative_url)

    @staticmethod
    def create_file_name(special_word: str, ext: str) -> str:
        """Create new file name

        Args:
            special_word (str): the special word to denote file name
            ext (str): the extention of the file

        Returns:
            str: the newly created file name
        """
        return f"media_{special_word}_{get_random_string(FilesProcessService.LENGTH_OF_FILE_NAME)}.{ext}"

    @abstractmethod
    def store_file() -> dict:
        pass

    @abstractmethod
    def delete_file():
        pass
