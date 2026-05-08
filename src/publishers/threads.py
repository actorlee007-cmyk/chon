from .base import BasePublisher
import logging
from ..utils.config_manager import ConfigManager

class ThreadsPublisher(BasePublisher):
    def __init__(self):
        self.config_manager = ConfigManager()

    def publish(self, video_path: str, metadata: dict):
        optimized = self.optimize_metadata(metadata)
        logging.info(f"Publishing to Threads: {optimized['content']}")
        return True

    def optimize_metadata(self, metadata: dict) -> dict:
        title = metadata['title'].replace("#shorts", "").strip()
        tags = self.config_manager.get_best_tags("Threads")
        tag_str = " ".join(tags)
        content = f"오늘의 한마디: {title}\n\n여러분은 어떻게 생각하시나요? {metadata['url']}\n\n{tag_str}"
        return {
            "content": content
        }
