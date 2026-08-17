from app.llm.model_manager import get_provider

class LLMClient:
    def __init__(self):
        self.provider = get_provider()

    def generate(self, messages, **kwargs):
        return self.provider.generate(messages, **kwargs)
