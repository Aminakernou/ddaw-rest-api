from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.category import Category
from pydantic import BaseModel

router = APIRouter(prefix="/categories", tags=["Categories"])

class CategoryCreate(BaseModel):
    name: str

# GET /categories → liste toutes les catégories
@router.get("/")
def get_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()

# GET /categories/{id} → une catégorie précise
@router.get("/{category_id}")
def get_category(category_id: int, db: Session = Depends(get_db)):
    cat = db.query(Category).filter(Category.id == category_id).first()
    if not cat:
        raise HTTPException(status_code=404, detail="Catégorie non trouvée")
    return cat

# POST /categories → créer une catégorie
@router.post("/", status_code=201)
def create_category(cat: CategoryCreate, db: Session = Depends(get_db)):
    existing = db.query(Category).filter(Category.name == cat.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Catégorie déjà existante")
    new_cat = Category(name=cat.name)
    db.add(new_cat)
    db.commit()
    db.refresh(new_cat)
    return new_cat

# PUT /categories/{id} → modifier une catégorie
@router.put("/{category_id}")
def update_category(category_id: int, updated: CategoryCreate, db: Session = Depends(get_db)):
    cat = db.query(Category).filter(Category.id == category_id).first()
    if not cat:
        raise HTTPException(status_code=404, detail="Catégorie non trouvée")
    cat.name = updated.name
    db.commit()
    db.refresh(cat)
    return cat

# DELETE /categories/{id} → supprimer une catégorie
@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    cat = db.query(Category).filter(Category.id == category_id).first()
    if not cat:
        raise HTTPException(status_code=404, detail="Catégorie non trouvée")
    db.delete(cat)
    db.commit()
    return {"message": f"Catégorie {category_id} supprimée"}