#!/use/bin/python3
"""
class user
"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """
    class of user
    """
    if models.storage_t == "db":
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        name = Column(String(128), nullable=True)
        age = Column(String(128), nullable=True)
        gender = Column(String(128), nullable=True)
        weight = Column(String(128), nullable=True)
        height = Column(String(128), nullable=True)
    else:
        email = ""
        password = ""
        name = ""
        age = ""
        gender = ""
        weight = ""
        height = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
