#!/usr/bin/python3
"""
DB Storage Engine
"""

from os import getenv
from models.base_model import BaseModel, Base
from models.article import Article
from models.programs import Programs
from models.user import User
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    """Represents a database storage engine.

    Attributes:
        __engine (sqlalchemy.Engine): The working SQLAlchemy engine.
        __session (sqlalchemy.Session): The working SQLAlchemy session.
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("MYSQL_USER"),
                                             getenv("MYSQL_PWD"),
                                             getenv("MYSQL_HOST"),
                                             getenv("MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        
    def all(self, cls=None):
        """Query on the curret database session all objects of the given class.
        If cls is None, queries all types of objects.
        Return:
            Dict of queried classes in the format <class name>.<obj id> = obj.
        """
        if cls is None:
            objs = self.__session.query(User).all()
            objs.extend(self.__session.query(Programs).all())
            objs.extend(self.__session.query(Article).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}
    
    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)
    
    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()
    
    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)
            self.save()
    
    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.close()
