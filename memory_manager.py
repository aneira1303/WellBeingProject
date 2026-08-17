from app.memory.conversation_memory import ConversationMemory
from app.memory.long_term_memory import LongTermMemory

class MemoryManager:
    def __init__(self):
        self.short_term = ConversationMemory()
        self.long_term = LongTermMemory()

    def add(self, user_id, role, content):
        self.short_term.add(user_id, role, content)

    def history(self, user_id):
        return self.short_term.get(user_id)
