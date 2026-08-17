from app.core.config import settings
from app.llm.providers.groq_provider import GroqProvider
from app.llm.providers.openai_provider import OpenAIProvider
from app.llm.providers.ollama_provider import OllamaProvider

def get_provider():
    if settings.LLM_PROVIDER == "openai":
        return OpenAIProvider()
    if settings.LLM_PROVIDER == "ollama":
        return OllamaProvider()
    return GroqProvider()
