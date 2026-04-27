from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base de données SQLite pour les tests en local
# Le membre 3 la remplacera par PostgreSQL dans Docker
SQLALCHEMY_DATABASE_URL = "sqlite:///./bibliotheque.db"

# Création du moteur de connexion
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # nécessaire pour SQLite
)

# Session pour interagir avec la base
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Classe de base pour tous les modèles ORM
Base = declarative_base()

# Dépendance FastAPI : ouvre et ferme la session automatiquement
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()