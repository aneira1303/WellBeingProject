from app.llm.prompts.system_prompts import SYSTEM_PROMPT
from app.llm.prompts.empathy_prompts import EMPATHY_PROMPT
from app.llm.prompts.wellness_prompts import WELLNESS_PROMPT
from app.llm.prompts.safety_prompts import SAFETY_PROMPT
from app.llm.prompts.rag_prompts import RAG_PROMPT


class PromptManager:

    def build(
        self,
        user_message: str,
        context: str = "",
        history=None
    ) -> list[dict]:

        system_prompt = "\n\n".join([
            SYSTEM_PROMPT,
            EMPATHY_PROMPT,
            WELLNESS_PROMPT,
            SAFETY_PROMPT,
            RAG_PROMPT
        ])

        if context:
            system_prompt += (
                f"\n\nRetrieved wellness context:\n{context}"
            )

        messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

        if history:
            messages.extend(history)

        messages.append({
            "role": "user",
            "content": user_message
        })

        return messages