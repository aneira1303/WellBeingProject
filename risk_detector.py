class RiskDetector:
    HIGH = [
        "kill myself", "end my life", "suicide", "take my life",
        "hurt myself", "self harm", "self-harm"
    ]
    MODERATE = [
        "can't cope", "cannot cope", "no hope", "worthless",
        "want to disappear", "hopeless"
    ]

    def detect(self, text):
        t = text.lower()
        if any(x in t for x in self.HIGH):
            return {"risk_level": "high", "matched": True}
        if any(x in t for x in self.MODERATE):
            return {"risk_level": "moderate", "matched": True}
        return {"risk_level": "low", "matched": False}
