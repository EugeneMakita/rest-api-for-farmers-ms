from abc import ABC, abstractmethod


class FilesProcessService(ABC):
    @abstractmethod
    def store_file():
        pass

    @abstractmethod
    def delete_file():
        pass
