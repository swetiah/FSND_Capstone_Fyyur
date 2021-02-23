from sqlalchemy import Column, Integer, String, DateTime, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
import os

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
'''


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Common(db.Model):
    __abstract__ = True

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class Venue(Common):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column("genres", db.ARRAY(db.String()))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref='venue',
                            lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'Venue ID {self.id} : Venue Name: {self.name}'
    
    def __init__(self,name,city,state,address,phone,genres,seeking_talent,seeking_description):
        self.name =name 
        self.city =city 
        self.state =state 
        self.address =address 
        self.phone =phone 
        self.genres =genres 
        self.seeking_talent =seeking_talent 
        self.seeking_description =seeking_description 
        self.shows = []


    
    def format(self):
        shows = []
        for show in self.shows:
            shows.append({
                'id':show.id,
            })
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'state': self.state,
            'address': self.address,
            'phone': self.phone,
            'genres': self.genres,
            'seeking_talent': self.seeking_talent,
            'seeking_description': self.seeking_description,
            'shows' : shows
        }


class Artist(Common):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column("genres", db.ARRAY(db.String()))
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref='artist', lazy=True)

    def __repr__(self):
        return f'Artist ID {self.id} : Artist Name: {self.name}'
    
    def __init__(self,name,city,state,phone,genres,seeking_venue,seeking_description):
        self.name =name 
        self.city =city 
        self.state =state 
        self.phone =phone 
        self.genres =genres 
        self.seeking_venue =seeking_venue 
        self.seeking_description =seeking_description 
        self.shows = []
    
    def format(self):
        shows = []
        for show in self.shows:
            shows.append({
                'id':show.id,
            })
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'state': self.state,
            'phone': self.phone,
            'genres': self.genres,
            'seeking_venue': self.seeking_venue,
            'seeking_description': self.seeking_description,
            'shows' : shows
        }


class Show(Common):
    __tablename__ = 'show'
    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey(
        'venue.id', ondelete='CASCADE'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey(
        'artist.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    
    def __init__(self,venueID,artistID,startTime):
        self.artist_id = artistID
        self.venue_id = venueID
        self.start_time = startTime


    def __repr__(self):
        return f'Show ID {self.id}'
