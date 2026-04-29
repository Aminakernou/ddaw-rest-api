from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.article import Article
from pydantic import BaseModel


router = APIRouter(prefix="/articles", tags=["Articles"])


class ArticleCreate(BaseModel):
    title: str
    content: str
    date: str
    auteur_id: int


@router.get("/")
def get_articles(db: Session = Depends(get_db)):
    return db.query(Article).all()


@router.get("/{article_id}")
def get_article(article_id: int, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == article_id).first()

    if not article:
        raise HTTPException(status_code=404, detail="Article not found")

    return article


@router.post("/")
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    new_article = Article(
        title=article.title,
        content=article.content,
        date=article.date,
        auteur_id=article.auteur_id
    )

    db.add(new_article)
    db.commit()
    db.refresh(new_article)

    return new_article


@router.put("/{article_id}")
def update_article(article_id: int, updated: ArticleCreate, db: Session = Depends(get_db)):
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


@router.delete("/{article_id}")
def delete_article(article_id: int, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == article_id).first()

    if not article:
        raise HTTPException(status_code=404, detail="Article not found")

    db.delete(article)
    db.commit()

    return {"message": "Article deleted"}