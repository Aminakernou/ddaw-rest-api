from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.article import Article

router = APIRouter(prefix="/articles", tags=["Articles"])

# GET all articles
@router.get("/")
def get_articles(db: Session = Depends(get_db)):
    return db.query(Article).all()


# GET article by id
@router.get("/{article_id}")
def get_article(article_id: int, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article


# CREATE article
@router.post("/")
def create_article(article: Article, db: Session = Depends(get_db)):
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


# UPDATE article
@router.put("/{article_id}")
def update_article(article_id: int, updated: Article, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == article_id).first()

    if not article:
        raise HTTPException(status_code=404, detail="Article not found")

    article.title = updated.title
    article.content = updated.content
    article.date = updated.date
    article.auteur_id = updated.auteur_id

    db.commit()
    db.refresh(article)
    return article


# DELETE article
@router.delete("/{article_id}")
def delete_article(article_id: int, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == article_id).first()

    if not article:
        raise HTTPException(status_code=404, detail="Article not found")

    db.delete(article)
    db.commit()
    return {"message": "Article deleted"}