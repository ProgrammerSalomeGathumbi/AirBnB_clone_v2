#!/usr/bin/python3
"""
DB storage class
"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

classes = {"City": City, "State": State, "User": User, "Place": Place,
           "Review": Review, "Amenity": Amenity}


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """initialize connection with MySQL"""
        db_uri = "{0}+{1}://{2}:{3}@{4}:3306/{5}".format(
            'mysql', 'mysqldb', getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'), getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')
        )

        self.__engine = create_engine(db_uri, pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query objects from the current database session"""
        entities = dict()

        if cls:
            return self.get_data_from_table(cls, entities)

        for entity in classes:
            entities = self.get_data_from_table(eval(entity), entities)

        return entities

    def new(self, obj):
        """add the object to the current database"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database"""
        if obj is not None:
            self.__session.delete(obj)

    def get_data_from_table(self, cls, structure):
        """Get the data from a MySQL Table
        """

        if type(structure) is dict:
            query = self.__session.query(cls)

            for _row in query.all():
                key = "{}.{}".format(cls.__name__, _row.id)
                structure[key] = _row

            return structure

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close session"""
        self.__session.close()
