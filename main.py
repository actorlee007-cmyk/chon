import time
import logging
from src.ingestors.youtube_watcher import YouTubeWatcher
from src.validator import ContentValidator
from src.scheduler import Scheduler
from src.publishers.instagram import InstagramPublisher
from src.publishers.tiktok import TikTokPublisher
from src.publishers.threads import ThreadsPublisher

from src.utils.video_processor import VideoProcessor

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OmniChannelSystem:
    def __init__(self):
        self.watcher = YouTubeWatcher(channel_id="CH_001")
        self.validator = ContentValidator()
        self.scheduler = Scheduler()
        self.processor = VideoProcessor()
        self.publishers = [
            InstagramPublisher(),
            TikTokPublisher(),
            ThreadsPublisher()
        ]

    def run_cycle(self):
        logging.info("Starting automation cycle...")
        new_shorts = self.watcher.check_for_new_shorts()
        
        for short in new_shorts:
            # 1. Validation (NR_014)
            if not self.validator.validate(short):
                logging.warning(f"Video {short['id']} failed validation. Skipping.")
                continue
            
            logging.info(f"Video {short['id']} validated. Proceeding to scheduling.")
            
            # 2. Scheduling & Processing & Publishing
            for pub in self.publishers:
                platform = pub.__class__.__name__.replace("Publisher", "")
                if self.scheduler.should_publish_now(platform):
                    # Physical transformation
                    processed_path = self.processor.process_for_platform(short['local_path'], platform)
                    # Publishing
                    pub.publish(processed_path, short)
                    logging.info(f"Successfully published to {platform}")
                else:
                    publish_time = self.scheduler.get_next_publish_time(platform)
                    logging.info(f"Scheduled for {platform} at {publish_time}")

    def evolve(self):
        """
        Placeholder for the self-evolving logic.
        Analyze shared-db analytics and update scheduler/metadata templates.
        """
        logging.info("Analyzing performance data for self-evolution...")
        # Logic to read from team-db and update local config would go here.
        pass

if __name__ == "__main__":
    system = OmniChannelSystem()
    system.run_cycle()
    system.evolve()
