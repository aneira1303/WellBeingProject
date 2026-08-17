from app.wellness.recommendations import Recommendations

class RecommendationAgent:
    def __init__(self):
        self.engine = Recommendations()

    def recommend(self, emotion):
        return self.engine.for_emotion(emotion)
