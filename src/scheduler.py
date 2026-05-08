import datetime
import json
import os
from .utils.config_manager import ConfigManager

class Scheduler:
    def __init__(self, analytics_path=None):
        self.analytics_path = analytics_path
        self.config_manager = ConfigManager()

    def get_next_publish_time(self, platform: str) -> datetime.datetime:
        now = datetime.datetime.now()
        peak_hours = self.config_manager.get_peak_hours(platform)
        
        for hour in sorted(peak_hours):
            candidate = datetime.datetime.combine(now.date(), datetime.time(hour, 0))
            if candidate > now:
                return candidate
        
        tomorrow = now + datetime.timedelta(days=1)
        first_peak = datetime.time(peak_hours[0], 0)
        return datetime.datetime.combine(tomorrow.date(), first_peak)

    def should_publish_now(self, platform: str) -> bool:
        now = datetime.datetime.now()
        peak_hours = self.config_manager.get_peak_hours(platform)
        # Check if we are within 30 minutes of any peak hour
        for hour in peak_hours:
            peak_time = datetime.datetime.combine(now.date(), datetime.time(hour, 0))
            if abs((now - peak_time).total_seconds()) < 1800:
                return True
        return False
