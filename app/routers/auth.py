from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import User
from app.utils import verify
from app.oauth2 import create_access_token
from app.schemas import Token


router = APIRouter(tags=['Authentication'])

@router.post('/login', response_model=Token)
async def login(user_credentials: OAuth2PasswordRequestForm=Depends(), db: Session=Depends(get_db)):
    user = db.query(User).filter(User.email==user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    # create token
    access_token = create_access_token(data={'user_id': user.id})
    # return token
    return {'access_token': access_token, 'token_type': 'bearer'}