#!/usr/bin/python3
"""
programs class
"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class programs(BaseModel, Base):
    """
    Representation of program class
    """
    if models.storage_t == "db":
        __tablename__ = 'programs'
        user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
        program_text = Column(String(1024), nullable=True)
        users = relationship("User", backref="user")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
