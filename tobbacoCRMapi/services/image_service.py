import base64
import os

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.utils.crypto import get_random_string
from PIL import Image

from ..helpers.file_helper import FileHelper
from .files_process_service import FilesProcessService


class ImageService(FilesProcessService):
    @staticmethod
    def store_file(request, base64_data: str) -> dict:
        """Store image

        Args:
            base64_data (str):

        Raises:
            ValueError: if the type of file is not allowed such as video etc

        Returns:
            tuple: this contains the url's of the small, medium and large resized images
        """
        (ext, img_str) = FileHelper.get_file_string_and_extension(base64_data)
        ImageService.validate_file_extentions(ext)
        return ImageService.save_image_to_disk(request, ext, img_str)

    @staticmethod
    def save_image_to_disk(request, ext: str, base64_content: str) -> dict:
        """Saves file to disk

        Args:
            base_file_name (str): the name of the file
            base64_content (str): Content of the base64 file
        """
        file_data = ContentFile(base64.b64decode(
            base64_content), name="temp." + ext)
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
        image_sizes = {"large": 1200, "medium": 600, "small": 300}
        data = {}
        with Image.open(file_data) as image:
            for name, height in image_sizes.items():
                data[name] = ImageService.save_variation_of_image(
                    height, image, name, ext, request
                )

        return data

    @staticmethod
    def save_variation_of_image(
        height: int, image, type: str, ext: str, request
    ) -> str:
        """Save a variation to disk and return url path

        Args:
            height (int): What should be the height of the image
            image (Image.Image): the image of
            type (str): the type of variation
            ext (str): The extension of the image
            request (_type_): the request information

        Returns:
            str: The url path of the saved file
        """
        resized_image = ImageService.resize_proportional(image, height)
        base_file_name = f"media_{type}_{get_random_string(16)}.{ext}"
        file_name = os.path.join(settings.MEDIA_ROOT, base_file_name)

        resized_image.save(file_name)
        return ImageService.get_absolute_url(request, base_file_name)

    @staticmethod
    def get_absolute_url(request, base_file_name) -> str:
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
    def validate_file_extentions(ext: str):
        """This checks if the file uploaded is the correct one

        Args:
            ext (str): The extention of the uploded file

        Raises:
            ValueError: This is raised when the file uploaded is the wrong ext
        """
        if ext not in ["jpeg", "jpg", "png", "gif"]:
            raise ValidationError("File should be a jpeg, png, jpg or a gif")

    @staticmethod
    def resize_proportional(image: Image.Image, base_height: int) -> Image.Image:
        """Scale an image

        Args:
            image (Image.Image): Image to be resized
            base_height (int): Height to which the image should be resized to

        Returns:
            Image.Image: The resized image
        """
        ratio = base_height / float(image.size[1])

        new_width = int(float(image.size[0]) * float(ratio))

        image = image.resize((new_width, base_height))
        return image

    @staticmethod
    def detete_file() -> bool:
        pass
