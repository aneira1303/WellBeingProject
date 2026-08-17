class EscalationManager:
    def action(self, risk_level):
        return "safety_response" if risk_level == "high" else "normal_response"
