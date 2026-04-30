from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class UserProfile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    bio = Column(String(255), nullable=True)       
    phone = Column(String(20), nullable=True)     
    adresse = Column(String(255), nullable=True)   
    avatar = Column(String(255), nullable=True)   

    # Clé étrangère vers users
    # unique=True → garantit le One-to-One 
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)

    # Relation inverse pour accéder au user depuis le profil
    user = relationship("User", back_populates="profile")
