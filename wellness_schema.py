from pydantic import BaseModel

class WellnessRequest(BaseModel):
    topic: str
    user_id: str = "anonymous"
