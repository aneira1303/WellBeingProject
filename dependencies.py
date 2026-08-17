from app.services.chat_service import ChatService

_chat_service = ChatService()

def get_chat_service() -> ChatService:
    return _chat_service
