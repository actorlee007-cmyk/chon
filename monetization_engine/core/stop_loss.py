class StopLossEngine:
    def __init__(self, threshold=-0.02):
        self.threshold = threshold

    def check_performance(self, current_metric, baseline_metric):
        """
        Check if performance has dropped below the threshold.
        current_metric: current ROI or ROAS
        baseline_metric: target or previous high ROI/ROAS
        """
        if baseline_metric == 0:
            return False
        
        drop_rate = (current_metric - baseline_metric) / baseline_metric
        
        if drop_rate <= self.threshold:
            return True # Trigger stop-loss
        return False

    def apply_rule(self, ad_id, performance_data):
        """
        Apply -2% stop-loss rule to a specific ad.
        """
        current_roas = performance_data.get('roas', 0)
        target_roas = performance_data.get('target_roas', 0)
        
        if self.check_performance(current_roas, target_roas):
            print(f"[STOP-LOSS] Ad {ad_id} triggered stop-loss. Current ROAS: {current_roas}, Target: {target_roas}")
            return "STOP"
        return "CONTINUE"
