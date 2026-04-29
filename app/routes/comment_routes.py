from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.comment import Comment
from app.models.article import Article
from app.models.user import User
from pydantic import BaseModel


router = APIRouter(prefix="/comments", tags=["Comments"])


class CommentCreate(BaseModel):
    body: str
    date: str
    article_id: int
    user_id: int


@router.get("/")
def get_comments(db: Session = Depends(get_db)):
    return db.query(Comment).all()


@router.get("/{comment_id}")
def get_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()

    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    return comment


@router.post("/")
def create_comment(comment: CommentCreate, db: Session = Depends(get_db)):

    article = db.query(Article).filter(
        Article.id == comment.article_id
    ).first()

    if not article:
        raise HTTPException(status_code=404, detail="Article not found")

    user = db.query(User).filter(
        User.id == comment.user_id
    ).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_comment = Comment(
        body=comment.body,
        date=comment.date,
        article_id=comment.article_id,
        user_id=comment.user_id
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return new_comment


@router.delete("/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()

    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    db.delete(comment)
    db.commit()

    return {"message": "Comment deleted"}


@router.get("/article/{article_id}")
def get_article_comments(article_id: int, db: Session = Depends(get_db)):
    comments = db.query(Comment).filter(
        Comment.article_id == article_id
    ).all()

    return comments