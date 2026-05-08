from .base import BasePublisher
import logging
from ..utils.config_manager import ConfigManager

class InstagramPublisher(BasePublisher):
    def __init__(self):
        self.config_manager = ConfigManager()

    def publish(self, video_path: str, metadata: dict):
        optimized = self.optimize_metadata(metadata)
        logging.info(f"Publishing to Instagram Reels: {optimized['title']}")
        return True

    def optimize_metadata(self, metadata: dict) -> dict:
        title = metadata['title'].replace("#shorts", "").strip()
        tags = self.config_manager.get_best_tags("Instagram")
        tag_str = " ".join(tags)
        return {
            "title": f"{title}\n\n{tag_str}",
            "description": metadata['description']
        }
