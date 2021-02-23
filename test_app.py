import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Artist, Venue, Show

Assistant = {
    'Content-Type': 'application/json',
    'Authorization': os.environ['Assistant_Token']
}


Manager = {
    'Content-Type': 'application/json',
    'Authorization': os.environ['Manager_token']
}

artist = {
            "name": "Mohammad",
            "city": "SA",
            "state": "SA",
            "phone": "111-111-1111",
            "genres": [],
            "seeking_venue": True,
            "seeking_description": "gfgfgfgf"
        }

venue = {
    "name": "self.name",
    "city": "self.city",
    "state": "self.state",
    "address": "self.address",
    "phone": "self.phone",
    "genres": [],
    "seeking_talent": False,
    "seeking_description": "self.seeking_description"
}

show = {
    "venue_id" : 1,
    "artist_id" : 1,
    "start_time" : "12/12/2012"
}

database_path = os.environ['DATABASE_URL']

class CapstoneTest(unittest.TestCase):
    """This class represents the capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ['DATABASE_URL']
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

# Successful Tests

    def test_get_artists(self):
        res = self.client().get('/artists',headers=Assistant)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
    
    def test_get_venues(self):
        res = self.client().get('/venues',headers=Assistant)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
    
    def test_get_shows(self):
        res = self.client().get('/shows',headers=Assistant)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_post_artist(self):
        res = self.client().post('/artists',headers=Manager,json=artist)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_post_venue(self):
        res = self.client().post('/venues',headers=Manager,json=venue)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_post_shows(self):
        res = self.client().post('/shows',headers=Manager,json=show)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_patch_artist(self):
        res = self.client().patch('/artists/1',headers=Manager,json={ 'name' : 'majed',})

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_patch_venue(self):
        res = self.client().patch('/venues/1',headers=Manager,json={ 'name' : 'Best venue'})

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
    
    def test_delete_artist(self):
        res = self.client().delete('/artists/2',headers=Manager)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_delete_venue(self):
        res = self.client().delete('/venues/2',headers=Manager)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

# Failed Tests

    def test_not_get_artists(self):
        res = self.client().get('/artists')

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
    
    def test_not_get_venues(self):
        res = self.client().get('/venues')

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
    
    def test_not_get_shows(self):
        res = self.client().get('/shows')

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)

    def test_not_post_artist(self):
        res = self.client().post('/artists',json=artist)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)

    def test_not_post_venue(self):
        res = self.client().post('/venues',json=venue)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)

    def test_not_post_shows(self):
        res = self.client().post('/shows',json=show)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)

    def test_not_patch_artist(self):
        res = self.client().patch('/artists/1',json={ 'name' : 'majed',})

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)

    def test_not_patch_venue(self):
        res = self.client().patch('/venues/1',json={ 'name' : 'Best venue'})

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
    
    def test_not_delete_artist(self):
        res = self.client().delete('/artists/2')

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)

    def test_not_delete_venue(self):
        res = self.client().delete('/venues/2')

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)


if __name__ == "__main__":
    unittest.main()
