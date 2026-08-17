from collections import defaultdict

class ShortTermMemory:
    def __init__(self, limit=12):
        self.limit = limit
        self.store = defaultdict(list)

    def add(self, user_id, role, content):
        self.store[user_id].append({"role": role, "content": content})
        self.store[user_id] = self.store[user_id][-self.limit:]

    def get(self, user_id):
        return self.store[user_id]
