from fastapi import Depends

from services.agent_service import AgentService  # Импорт AgentService

def get_agent_service():
    """
    Заглушка для dependency injection AgentService.
    Реальная реализация будет создана позже.
    """
    return AgentService()  # Просто возвращаем экземпляр AgentService (заглушку)


from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = decode_jwt(token)
        user_id: UUID = payload.get("sub")
        if not user_id:
            raise CredentialsException()
    except JWTError:
        raise CredentialsException()
    
    user = await user_service.get_user(user_id)
    if not user:
        raise CredentialsException()
        
    return user
