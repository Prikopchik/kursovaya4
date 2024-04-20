from abc import ABC, abstractmethod

class DataSaverLoader(ABC):
    @abstractmethod
    def save_data(self, data, file_path) -> None:
        pass
    
    @abstractmethod
    def load_data(self, file_path):
        pass
