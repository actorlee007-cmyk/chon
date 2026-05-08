from core.ad_manager import AdManager
from core.stop_loss import StopLossEngine
from core.funnel_tracker import FunnelTracker
from core.optimizer import FunnelOptimizer
from core.profit_tracker import ProfitTracker
import time

def run_monetization_cycle(profit_tracker):
    print("--- Starting Monetization Optimization Cycle ---")
    
    # 1. Initialize components
    ad_manager = AdManager()
    stop_loss = StopLossEngine()
    tracker = FunnelTracker()
    optimizer = FunnelOptimizer(tracker)
    
    # 2. Simulate Analytics Data (from DataAnalyticsEngine in the future)
    mock_analytics = [
        {'id': 'ad_001', 'ctr': 0.02, 'retention': 0.4},
        {'id': 'ad_002', 'ctr': 0.05, 'retention': 0.6},
        {'id': 'ad_003', 'ctr': 0.01, 'retention': 0.3}
    ]
    
    # 3. Select Best Creative
    best_ad = ad_manager.select_best_creative(mock_analytics)
    print(f"[ACTION] Best creative selected: {best_ad['id']}")
    
    # 4. Inject Budget
    spend = 50000
    ad_manager.inject_budget(best_ad['id'], spend) 
    profit_tracker.add_spend(spend)
    
    # 5. Simulate Performance & Stop-Loss
    # Let's say ad_002 started strong but dropped
    performance_data = {'roas': 1.5, 'target_roas': 2.0}
    action = stop_loss.apply_rule(best_ad['id'], performance_data)
    
    if action == "STOP":
        print(f"[ACTION] Pausing Ad {best_ad['id']} due to -2% rule.")
    
    # 6. Simulate Funnel Tracking & Revenue
    tracker.track_event('landing_page_views')
    tracker.track_event('landing_page_views')
    tracker.track_event('signups')
    tracker.track_event('checkout_started')
    tracker.track_event('payments_completed')
    
    # Simulate a payment of 100,000 KRW
    revenue = 100000
    profit_tracker.add_revenue(revenue)
    
    tracker.report()
    profit_tracker.report()
    
    # 7. Funnel Optimization
    optimizer.optimize()
    optimizer.auto_adjust_landing_page(best_ad['id'])
    
    print("--- Cycle Complete ---")

if __name__ == "__main__":
    p_tracker = ProfitTracker()
    while True:
        run_monetization_cycle(p_tracker)
        print("\nSleeping for 10 seconds (Simulation mode)...\n")
        time.sleep(10)
