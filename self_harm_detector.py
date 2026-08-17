from app.safety.risk_detector import RiskDetector

class SelfHarmDetector:
    def detect(self, text):
        return RiskDetector().detect(text)["risk_level"] == "high"
