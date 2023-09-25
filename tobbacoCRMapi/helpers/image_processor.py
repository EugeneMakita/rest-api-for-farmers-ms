import base64
import os

from django.conf import settings
from django.core.files.base import ContentFile
from django.utils.crypto import get_random_string
from PIL import Image


class ImageProcessor:
    @staticmethod
    def get_image_string_and_extension(base_64_string: str) -> tuple:
        """Get the image string from base 64 and the extension

        Args:
            base_64_string (str): this is the base 64 string to be converteed to image

        Returns:
            tuple: extenstion of image and the image string
        """
        format_str, imgstr = base_64_string.split(';base64,')
        return format_str.split('/')[-1], imgstr

    @staticmethod
    def store_image(base64_data: str) -> tuple:
        """ Store image 

        Args:
            base64_data (str):

        Raises:
            ValueError: if the type of file is not allowed such as video etc

        Returns:
            tuple: this contains the url's of the small, medium and large resized images
        """
        (ext, imgstr) = ImageProcessor.get_image_string_and_extension(base64_data)
        if ext not in ["jpeg", "jpg", "png", "gif"]:
            raise ValueError('File should be a jpeg, png, jpg or a gif')

        file_data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        image = Image.open(file_data)
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
        image_sizes = {"large": 1200, "medium": 600, "small": 300}
        data = {}
        for name, height in image_sizes.items():
            resized_image = ImageProcessor.resize_proportional(image, height)
            file_name = os.path.join(
                settings.MEDIA_ROOT, f'media_{name}_{get_random_string(16)}.{ext}')
            resized_image.save(file_name)
            data[name] = file_name

        return data

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
