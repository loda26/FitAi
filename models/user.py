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
        name = Column(String(128), nullable=False)
        age = Column(String(128), nullable=False)
        gender = Column(String(128), nullable=False)
        weight = Column(String(128), nullable=False)
        height = Column(String(128), nullable=False)
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
