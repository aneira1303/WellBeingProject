class WellnessAgent:
    def instructions(self, topic):
        return {
            "topic": topic,
            "message": "Choose a small, manageable wellness activity and stop if it makes you uncomfortable."
        }
