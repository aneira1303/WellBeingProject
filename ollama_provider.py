import requests
from app.core.config import settings
from app.llm.providers.base_provider import BaseLLMProvider
from app.core.exceptions import LLMProviderError

class OllamaProvider(BaseLLMProvider):
    def generate(self, messages, **kwargs):
        prompt = "\n".join(f"{m['role']}: {m['content']}" for m in messages)
        try:
            r = requests.post(
                f"{settings.OLLAMA_BASE_URL}/api/generate",
                json={"model": settings.OLLAMA_MODEL, "prompt": prompt, "stream": False},
                timeout=120,
            )
            r.raise_for_status()
            return r.json().get("response", "")
        except Exception as exc:
            raise LLMProviderError(str(exc))
