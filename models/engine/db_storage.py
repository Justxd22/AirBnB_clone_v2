#!/usr/bin/python3
"""Sql Storage engine."""
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
import models
import os


class DBStorage:
    """New SQL eng."""
    __engine = None
    __session = None

    def __init__(self):
        """New SQL eng."""
        env = os.getenv("HBNB_ENV")
        user = os.getenv("HBNB_MYSQL_USER")
        passw = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passw, host, db),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Get a dict of all obj."""
        d = {}
        if not cls:
            lists = [models.State, models.City, models.User,
                     models.Place, models.Review, models.Amenity]
            for classes in lists:
                q = self.__session.query(classes)
                for ele in q:
                    d["{}.{}".format(type(ele).__name__, ele.id)] = ele
        else:
            if type(cls) is str:
                cls = eval(cls)
            q = self.__session.query(cls)
            for ele in q:
                d["{}.{}".format(type(ele).__name__, ele.id)] = ele
        return (d)

    def new(self, obj):
        """Add new key to the Objects dict."""
        self.__session.add(obj)

    def save(self):
        """Save Objects dict into json file."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an existing element."""
        if obj:
            self.session.delete(obj)

    def reload(self):
        """Loads storage dictionary from file."""
        Base.metadata.create_all(self.__engine)
        s = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(s)
        self.__session = Session()

    def close(self):
        """Close session."""
        self.__session.close()
