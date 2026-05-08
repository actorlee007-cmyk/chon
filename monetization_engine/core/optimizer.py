class FunnelOptimizer:
    def __init__(self, tracker):
        self.tracker = tracker

    def optimize(self):
        rates = self.tracker.get_conversion_rates()
        recommendations = []

        if rates.get('view_to_signup', 0) < 0.05:
            recommendations.append("Hero section of landing page needs improvement (Low CTR).")
        
        if rates.get('signup_to_checkout', 0) < 0.2:
            recommendations.append("Onboarding process is too long. Simplify it.")

        if rates.get('checkout_to_payment', 0) < 0.5:
            recommendations.append("Payment friction detected. Add more payment methods or trust badges.")

        if recommendations:
            print("[OPTIMIZER] Recommendations for improvement:")
            for rec in recommendations:
                print(f" - {rec}")
        else:
            print("[OPTIMIZER] Funnel is performing optimally.")
            
        return recommendations

    def auto_adjust_landing_page(self, best_creative_id):
        """
        Self-evolving logic: Update landing page hero image/text to match 
        the best performing ad creative automatically.
        """
        print(f"[OPTIMIZER] Auto-adjusting landing page elements based on best creative: {best_creative_id}")
        # In a real system, this would trigger a CI/CD or CMS update
