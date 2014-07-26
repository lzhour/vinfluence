from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from urllib2 import urlopen
import requests

API_KEY = 'c02a2b186d8415fbd1ea09519abffa5a'

ENGINE = None
Session = None

ENGINE = create_engine("sqlite:///winelist.db", echo = False)
dbsession = scoped_session(sessionmaker(bind = ENGINE,
                                    autocommit = False,
                                    autoflush = False))

Base = declarative_base()
Base.query = dbsession.query_property()

class WineObject(Base):
    __tablename__ = "wineobject"

    id = Column(Integer, primary_key = True)
    wine_type = Column(String(64), nullable=True)
    varietal = Column(String(64), nullable=True)
    region = Column(String(300), nullable=True)
    description = Column(String(100), nullable=True)
    cheese_pairing = Column(String(500), nullable=True)
    food_pairing = Column(String(300), nullable=True)
    fruit_pairing = Column(String(200), nullable=True)
    flavor_profile = Column(String(200), nullable=True)
    flavor_pairing = Column(String(200), nullable=True)
    img_path = Column(String(100), nullable=True)
    api_id = Column(String(50), nullable=True)

def createTable():
    Base.metadata.create_all(ENGINE)

def get_wine_types(wine_type):
    cursor = connect()
    wine_type = wine_type.capitalize()
    varietals = dbsession.query(WineObject).filter_by(wine_type=wine_type).all()
    return varietals

def get_varietal(wine_id):
    cursor = connect()
    varietal_desc = dbsession.query(WineObject).filter_by(id=wine_id).all()
    return varietal_desc

def get_api_parameters(wine_id):
    cursor = connect()
    wine_object = dbsession.query(WineObject).filter_by(id=wine_id).all()
    return wine_object[0].api_id

def make_api_call(wine_id):
    # varietal_objects = get_varietal(wine_id)
    parameters = get_api_parameters(wine_id)
    url = 'http://services.wine.com/api/beta2/service.svc/json/catalog?filter=categories(490+'+parameters+')&filter=rating(93|100)&apikey='+API_KEY
    api_request = requests.get(url).json()
    return api_request

def connect():
    global dbsession
    return dbsession()

def main():
    # createTable()
    pass
    
if __name__ == "__main__":
    main()