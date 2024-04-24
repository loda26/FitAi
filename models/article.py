#!/bin/usr/python3
"""
Article Class
"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class Article(BaseModel, Base):
    """
    Representation of article class
    """
    if models.storage_t == "db":
        __tablename__ = 'article'
        title = Column(String(1024), nullable=True)
        article_text = Column(String(1024), nullable=True)
        image_path = Column(String(1024), nullable=True)
    else:
        title = ""
        article_text = ""
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
