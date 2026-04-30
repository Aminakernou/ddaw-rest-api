from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from app.database import get_db
from app.models.user import User
from app.models.profile import UserProfile
from pydantic import BaseModel, EmailStr

router = APIRouter()



class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str = "membre"

class UserUpdate(BaseModel):
    name: str
    email: str
    role: str

class ProfileCreate(BaseModel):
    bio: Optional[str] = None
    phone: Optional[str] = None
    adresse: Optional[str] = None
    avatar: Optional[str] = None

class ProfileUpdate(BaseModel):
    bio: Optional[str] = None
    phone: Optional[str] = None
    adresse: Optional[str] = None
    avatar: Optional[str] = None
─
# Routes USERS


# GET /users → liste tous les utilisateurs
@router.get("/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


# GET /users/{id} → retourne un utilisateur précis
@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return user


# POST /users → créer un nouvel utilisateur
@router.post("/", status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Vérifier si l'email est déjà utilisé
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email déjà utilisé")

    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password,  
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# PUT /users/{id} → modifier un utilisateur
@router.put("/{user_id}")
def update_user(user_id: int, updated: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    # Vérifier que le nouvel email n'est pas pris par un autre user
    existing = db.query(User).filter(User.email == updated.email, User.id != user_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email déjà utilisé")

    user.name = updated.name
    user.email = updated.email
    user.role = updated.role
    db.commit()
    db.refresh(user)
    return user



