#!/usr/bin/python3
"""
New Engine
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class DBStorage:
    """
    New Engine
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Instantiates instances with attributes"""
        # dialect+driver://username:password@host:port/database
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                      .format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
                                              pool_pre_ping=True)
