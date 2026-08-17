class LongTermMemory:
    def __init__(self):
        self.preferences = {}

    def set(self, user_id, key, value):
        self.preferences.setdefault(user_id, {})[key] = value

    def get(self, user_id):
        return self.preferences.get(user_id, {})
