from fastapi import FastAPI
from app.database import Base, engine

# Import des modèles (important)
from app.models.user import User
from app.models.profile import UserProfile
from app.models.article import Article
from app.models.category import Category
from app.models.comment import Comment

# Import des routes
from app.routes import user_routes
from app.routes import article_routes
from app.routes import category_routes
from app.routes import comment_routes

# Création des tables APRÈS import des modèles
Base.metadata.create_all(bind=engine)

app = FastAPI(title="DDAW REST API")

app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(article_routes.router, prefix="/articles", tags=["Articles"])
app.include_router(category_routes.router)
app.include_router(comment_routes.router)


@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API DDAW"}