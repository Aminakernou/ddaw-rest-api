from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base
article_category = Table(
    "article_category",
    Base.metadata,
    Column("article_id", Integer, ForeignKey("articles.id")),
    Column("category_id", Integer, ForeignKey("categories.id"))
)
class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    date = Column(String(50), nullable=True)

    # clé étrangère vers User
    auteur_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", backref="articles")

    categories = relationship(
    "Category",
    secondary=article_category,
    back_populates="articles"
)