from fastapi import FastAPI
from app.database import Base, engine
from app.routes import user_routes
from app.routes import article_routes
from app.routes import category_routes
Base.metadata.create_all(bind=engine)

app = FastAPI(title="DDAW REST API")

app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(article_routes.router, prefix="/articles", tags=["Articles"])
app.include_router(category_routes.router, prefix="/categories", tags=["Categories"])
@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API DDAW"}