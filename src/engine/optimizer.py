
import os
import json

class TrendOptimizer:
    """
    DataAnalyticsEngine의 분석 결과를 바탕으로 트렌드 추출 로직을 스스로 강화
    """
    def __init__(self):
        self.analytics_path = "/home/team/shared/analytics_results.json"
        self.priority_keywords = []

    def load_feedback(self):
        if os.path.exists(self.analytics_path):
            try:
                with open(self.analytics_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # 성공 확률이 높은 키워드 추출 로직
                    self.priority_keywords = data.get("successful_keywords", [])
                print(f"Loaded {len(self.priority_keywords)} priority keywords from analytics.")
            except Exception as e:
                print(f"Error loading feedback: {e}")

    def score_trend(self, trend_title: str) -> float:
        score = 1.0
        for keyword in self.priority_keywords:
            if keyword.lower() in trend_title.lower():
                score += 0.5
        return score
