class FunnelTracker:
    def __init__(self):
        self.funnel_data = {
            'landing_page_views': 0,
            'signups': 0,
            'checkout_started': 0,
            'payments_completed': 0
        }

    def track_event(self, event_name):
        if event_name in self.funnel_data:
            self.funnel_data[event_name] += 1
        else:
            print(f"[ERROR] Unknown event: {event_name}")

    def get_conversion_rates(self):
        rates = {}
        if self.funnel_data['landing_page_views'] > 0:
            rates['view_to_signup'] = self.funnel_data['signups'] / self.funnel_data['landing_page_views']
        
        if self.funnel_data['signups'] > 0:
            rates['signup_to_checkout'] = self.funnel_data['checkout_started'] / self.funnel_data['signups']
            
        if self.funnel_data['checkout_started'] > 0:
            rates['checkout_to_payment'] = self.funnel_data['payments_completed'] / self.funnel_data['checkout_started']
            
        return rates

    def report(self):
        print(f"[FUNNEL] Current Data: {self.funnel_data}")
        print(f"[FUNNEL] Conversion Rates: {self.get_conversion_rates()}")
