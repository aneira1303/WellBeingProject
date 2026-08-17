from app.llm.providers.base_provider import BaseLLMProvider
from app.core.config import settings
from app.core.exceptions import LLMProviderError

class GroqProvider(BaseLLMProvider):
    def __init__(self):
        try:
            from openai import OpenAI
            self.client = OpenAI(
                api_key=settings.GROQ_API_KEY,
                base_url="https://api.groq.com/openai/v1"
            )
        except Exception as exc:
            raise LLMProviderError(str(exc))

    def generate(self, messages, **kwargs):
        if not settings.GROQ_API_KEY:
            raise LLMProviderError("GROQ_API_KEY is not configured.")
        response = self.client.chat.completions.create(
            model=settings.LLM_MODEL,
            messages=messages,
            temperature=kwargs.get("temperature", 0.5),
            max_tokens=kwargs.get("max_tokens", 700),
        )
        return response.choices[0].message.content or ""
