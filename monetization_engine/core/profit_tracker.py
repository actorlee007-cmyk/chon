class ProfitTracker:
    def __init__(self, monthly_fixed_cost=3000000):
        self.fixed_cost = monthly_fixed_cost
        self.total_revenue = 0
        self.total_ad_spend = 0

    def add_revenue(self, amount):
        self.total_revenue += amount

    def add_spend(self, amount):
        self.total_ad_spend += amount

    def get_status(self):
        net_profit = self.total_revenue - self.total_ad_spend
        offset_progress = (net_profit / self.fixed_cost) * 100
        
        status = {
            "revenue": self.total_revenue,
            "ad_spend": self.total_ad_spend,
            "net_profit": net_profit,
            "fixed_cost": self.fixed_cost,
            "offset_percentage": offset_progress
        }
        return status

    def report(self):
        status = self.get_status()
        print(f"[PROFIT] Revenue: {status['revenue']} KRW")
        print(f"[PROFIT] Ad Spend: {status['ad_spend']} KRW")
        print(f"[PROFIT] Net Profit: {status['net_profit']} KRW")
        print(f"[PROFIT] Offset Progress: {status['offset_percentage']:.2f}% of 3M fixed cost.")
        
        if status['net_profit'] >= status['fixed_cost']:
            print("[PROFIT] GOAL REACHED: Fixed costs are fully offset!")
