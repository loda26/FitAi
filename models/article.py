#!/bin/usr/python3
"""
Article Class
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Article(BaseModel, Base):
    __tablename__ = 'article'

    title = Column(String(1024), nullable=True)
    article_text = Column(String(1024), nullable=True)
    image_path = Column(String(1024), nullable=True)
