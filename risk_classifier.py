from app.safety.risk_detector import RiskDetector

class RiskClassifier:
    def predict(self, text):
        return RiskDetector().detect(text)
