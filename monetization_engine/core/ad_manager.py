import random

class AdManager:
    def __init__(self):
        self.ads = {} # ad_id: {creative, budget, performance}

    def select_best_creative(self, analytics_data):
        """
        Select the best creative based on CTR and retention from analytics data.
        """
        if not analytics_data:
            return None
        
        # Sort creatives by a combined score of CTR and engagement
        best_creative = max(analytics_data, key=lambda x: (x.get('ctr', 0) * 0.7 + x.get('retention', 0) * 0.3))
        return best_creative

    def inject_budget(self, ad_id, amount, balance_limit=3000000):
        """
        Inject budget into an ad campaign.
        Ensures it doesn't exceed the 3M KRW fixed cost offset goal if needed, 
        but here it's more about strategic allocation.
        """
        if ad_id not in self.ads:
            self.ads[ad_id] = {'budget': 0}
        
        self.ads[ad_id]['budget'] += amount
        print(f"[BUDGET] Injected {amount} into Ad {ad_id}. Total: {self.ads[ad_id]['budget']}")

    def get_performance_report(self):
        # In a real scenario, this would fetch from Meta/Google Ads API
        return self.ads
