import json
import os

class ConfigManager:
    def __init__(self, config_path="config/performance.json"):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                return json.load(f)
        return {}

    def save_config(self, new_config):
        self.config = new_config
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=2)

    def get_best_tags(self, platform):
        return self.config.get("best_hashtags", {}).get(platform, [])

    def get_peak_hours(self, platform):
        return self.config.get("peak_hours", {}).get(platform, [])
