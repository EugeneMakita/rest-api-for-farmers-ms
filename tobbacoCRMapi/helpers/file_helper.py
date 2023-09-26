class FileHelper:
    @staticmethod
    def get_file_string_and_extension(base_64_string: str) -> tuple:
        """Get the file string from base 64 and the extension

        Args:
            base_64_string (str): this is the base 64 string to be converteed to file

        Returns:
            tuple: extenstion of file and the file string
        """
        format_str, file_str = base_64_string.split(";base64,")
        return format_str.split("/")[-1], file_str
