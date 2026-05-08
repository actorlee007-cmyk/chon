import time
import logging

class YouTubeWatcher:
    def __init__(self, channel_id: str):
        self.channel_id = channel_id
        self.last_checked_video_id = None

    def check_for_new_shorts(self):
        """
        Polls YouTube API for new Shorts in the channel.
        Returns a list of metadata for new shorts.
        """
        # In real life, use google-api-python-client
        logging.info(f"Checking YouTube channel {self.channel_id} for new shorts...")
        
        # Mocking finding a new video
        new_video = {
            "id": "mock_vid_123",
            "title": "12차원 사고의 비밀 #shorts",
            "description": "세상을 바꾸는 12차원 사고법에 대해 알아봅니다.",
            "url": "https://youtube.com/shorts/mock_vid_123",
            "local_path": "/tmp/mock_video.mp4" # Assume it's downloaded
        }
        
        # In a real loop, we would compare with self.last_checked_video_id
        return [new_video]
