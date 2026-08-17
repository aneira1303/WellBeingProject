from app.wellness.recommendations import Recommendations

class RecommendationEngine:
    def __init__(self):
        self.engine = Recommendations()

    def generate(self, emotion):
        return self.engine.for_emotion(emotion)
