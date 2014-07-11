from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

ENGINE = None
Session = None

ENGINE = create_engine("sqlite:///winelist.db", echo = False)
dbsession = scoped_session(sessionmaker(bind = ENGINE,
                                    autocommit = False,
                                    autoflush = False))

Base = declarative_base()
Base.query = dbsession.query_property()

### Class declarations go here
class WineObject(Base):
    __tablename__ = "wineobject"

    id = Column(Integer, primary_key = True)
    wine_type = Column(String(64), nullable=True)
    varietal = Column(String(64), nullable=True)
    flavor_profile = Column(String(300), nullable=True)
    region = Column(String(100), nullable=True)
    description = Column(String(500), nullable=True)
    cheese_pairing = Column(String(300), nullable=True)
    food_pairing = Column(String(200), nullable=True)
    fruit_pairing = Column(String(200), nullable=True)
    flavor_pairing = Column(String(200), nullable=True)


def createTable():
    Base.metadata.create_all(ENGINE)

def connect():
    global dbsession
    return dbsession()

def main():
    createTable()
    
if __name__ == "__main__":
    main()