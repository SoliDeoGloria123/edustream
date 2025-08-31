"""
Middleware de autenticación y autorización para FastAPI.
"""
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Callable # noqa: F401
import jwt  # type: ignore
import os

SECRET_KEY = os.getenv("SECRET_KEY")

# Middleware de autenticación usando JWT
class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True, allowed_roles=None):
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self.allowed_roles = allowed_roles or []

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            payload = self.verify_jwt(credentials.credentials)
            if not payload:
                raise HTTPException(status_code=403, detail="Invalid or expired token.")
            # Verificar rol si se requiere
            if self.allowed_roles and payload.get("role") not in self.allowed_roles:
                raise HTTPException(status_code=403, detail="Insufficient permissions.")
            return payload
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, token: str) -> dict:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return payload
        except Exception:
            return None

# Explicación:
# - Este middleware verifica el JWT en el header Authorization.
# - Si el token es válido y el rol está permitido, deja pasar la petición.
# - Si no, lanza un error 403.
# - Puedes usarlo en tus rutas así:
#   @router.get("/admin", dependencies=[Depends(JWTBearer(allowed_roles=["admin"]))])
# - Así solo los usuarios con rol "admin" pueden acceder a esa ruta.
