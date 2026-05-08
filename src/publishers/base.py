from abc import ABC, abstractmethod

class BasePublisher(ABC):
    @abstractmethod
    def publish(self, video_path: str, metadata: dict):
        pass

    @abstractmethod
    def optimize_metadata(self, metadata: dict) -> dict:
        pass
