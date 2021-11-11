from sqlalchemy.orm import Session
from . import models, schemas
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional









SECRET_KEY = "07c5825dd6afbc09da756d879ef9d6ade3a10a1276d3ff100b57ea90e8f18199"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db, username: str):
    return db.query(models.User).filter(models.User.username== username).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username,hashed_password=get_password_hash(user.password), email = user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_post(db: Session,user_id:int,title:str,body:str, url:str):
    db_post = models.Post(title=title,body=body,owner_id=user_id, url = url)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_post(db, id: int):
    return db.query(models.Post).filter(models.Post.id== id).first()

def post_list(db):
    return db.query(models.Post).all()


def create_comment(db: Session,post_id:int,comment:schemas.CommentBase):
    db_comment = models.Comment(post_id=post_id,**comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

