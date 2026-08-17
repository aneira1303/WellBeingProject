from pydantic import BaseModel

class JournalEntry(BaseModel):
    user_id: str = "anonymous"
    text: str
