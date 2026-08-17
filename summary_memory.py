class SummaryMemory:
    def __init__(self):
        self.summaries = {}

    def set(self, user_id, summary):
        self.summaries[user_id] = summary

    def get(self, user_id):
        return self.summaries.get(user_id, "")
