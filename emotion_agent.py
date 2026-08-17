from app.emotion.emotion_detector import EmotionDetector

class EmotionAgent:
    def __init__(self):
        self.detector = EmotionDetector()

    def analyze(self, text):
        return self.detector.detect(text)
