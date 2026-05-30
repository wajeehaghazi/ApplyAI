from jose import JWTError, jwt
from backend.config.settings import settings
from backend.utils.custom_exceptions import AuthenticationError
from fastapi import Header

ALGORITHM = "HS256"

def verify_jwt_token(token: str) -> str:
    """Verifies the JWT token and returns the user ID if valid."""

    try:
        payload= jwt.decode(
            token, 
            settings.JWT_SECRET_KEY,
            algorithms= [ALGORITHM]
        )

        user_id: str= payload.get("sub")

        if not user_id:
            raise AuthenticationError("Invalid token: Missing user ID")
        return user_id
    
    except JWTError:
        raise AuthenticationError("Invalid token: JWT decoding failed")
    

def get_current_user(
    authorization: str = Header(...)) -> str:
    """
    Extract Bearer token from Authorization header
    and return authenticated user_id.
    """

    if not authorization.startswith("Bearer "):
        raise AuthenticationError(
            "Invalid authorization header."
        )

    token = authorization.replace(
        "Bearer ",
        ""
    )

    return verify_jwt_token(token)