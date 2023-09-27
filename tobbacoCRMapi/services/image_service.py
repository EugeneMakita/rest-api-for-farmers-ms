import base64
import os

from django.conf import settings
from django.core.files.base import ContentFile
from PIL import Image
from rest_framework.request import Request

from ..helpers.file_helper import FileHelper
from .files_process_service import FilesProcessService


class ImageService(FilesProcessService):
    FILE_EXTENSIONS = ["jpeg", "jpg", "png", "gif"]
    IMAGE_SIZES = {"large": 1200, "medium": 600, "small": 300}

    @staticmethod
    def store_file(request: Request, base64_data: str) -> dict:
        """Store image

        Args:
            base64_data (str):

        Raises:
            ValueError: if the type of file is not allowed such as video etc

        Returns:
            dict: this contains the url's of the small, medium and large resized images
        """
        (ext, img_str) = FileHelper.get_file_string_and_extension(base64_data)
        ImageService.validate_file_extentions(ImageService, ext)
        return ImageService.save_file_to_disk(request, ext, img_str)

    @staticmethod
    def save_file_to_disk(request: Request, ext: str, base64_content: str) -> dict:
        """Saves file to disk

        Args:
            base_file_name (str): the name of the file
            base64_content (str): Content of the base64 file
        """
        file_data = ContentFile(base64.b64decode(
            base64_content), name="temp." + ext)
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
        data = {}
        with Image.open(file_data) as image:
            for name, height in ImageService.IMAGE_SIZES.items():
                data[name] = ImageService.save_variation_of_image(
                    height, image, name, ext, request
                )

        return data

    @staticmethod
    def save_variation_of_image(
        height: int, image, type: str, ext: str, request: Request
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
        base_file_name = ImageService.create_file_name(type, ext)
        file_name = os.path.join(settings.MEDIA_ROOT, base_file_name)
        resized_image.save(file_name)
        return ImageService.get_absolute_url(request, base_file_name)

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
    def delete_file(image) -> None:
        os.remove(ImageService.get_full_path(image.large))
        os.remove(ImageService.get_full_path(image.small))
        os.remove(ImageService.get_full_path(image.medium))

    @staticmethod
    def get_full_path(base_file: str) -> str:
        base_file_name = base_file.split("/")[-1]
        return os.path.join(settings.MEDIA_ROOT, base_file_name)
