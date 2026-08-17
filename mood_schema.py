from pydantic import BaseModel

class MoodEntry(BaseModel):
    user_id: str = "anonymous"
    mood: str
    score: int = 5
