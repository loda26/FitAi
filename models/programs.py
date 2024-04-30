#!/usr/bin/python3
"""
programs class
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Programs(BaseModel, Base):
    __tablename__ = 'programs'

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    program_text = Column(String(1024), nullable=True)
    client_type = Column(String(60), nullable=True)
