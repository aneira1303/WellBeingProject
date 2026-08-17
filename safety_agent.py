from app.safety.risk_detector import RiskDetector

class SafetyAgent:
    def __init__(self):
        self.detector = RiskDetector()

    def analyze(self, text):
        return self.detector.detect(text)
