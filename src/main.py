
import sys
import os
import json
from crawler.business_trends import BusinessTrendCrawler
from engine.philosopher import ChairmanPhilosophy

class TrendIntelligenceEngine:
    def __init__(self):
        self.crawler = BusinessTrendCrawler()
        self.philosophy = ChairmanPhilosophy()
        self.output_path = "/home/team/shared/unit3_trends.json"

    def run(self):
        print("Starting Trend Intelligence Engine...")
        
        # 1. Crawl
        print("Crawling global top 1% business trends...")
        raw_trends = self.crawler.crawl()
        
        # 2. Filter & Process (Philosophy & Self-Censorship NR_014)
        print("Applying Chairman's philosophy and NR_014 self-censorship...")
        processed_trends = []
        for trend in raw_trends:
            if self.philosophy.is_aligned(trend['title']):
                trend['analyzed_content'] = self.philosophy.apply_philosophy(trend['title'])
                trend['status'] = "Verified (NR_014)"
                processed_trends.append(trend)
            else:
                print(f"Skipping trend (not aligned): {trend['title']}")

        # 3. Integrate (Unit 3 Pipeline)
        print(f"Exporting {len(processed_trends)} trends to Unit 3 process...")
        self.save_to_unit3(processed_trends)
        
        print("Execution completed.")

    def save_to_unit3(self, data):
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Successfully saved trends to {self.output_path}")
        except Exception as e:
            print(f"Error saving to Unit 3: {e}")

if __name__ == "__main__":
    engine = TrendIntelligenceEngine()
    engine.run()
