class SupervisorAgent:
    def route(self, risk_level, emotion):
        if risk_level == "high":
            return "safety"
        if emotion in {"sad", "anxious", "stressed", "lonely"}:
            return "wellness"
        return "conversation"
