'''
These Test classes test the business logic of users and movie
views and models.
'''

import unittest
import re

from flask_pymongo import PyMongo

import app as app_module

app = app_module.app

# Setting up test DB on Mongo and switching CSRF checks off
app.config["TESTING"] = True
app.config["WTF_CSRF_ENABLED"] = False
app.config['MONGO_URI'] = 'mongodb://localhost:27017/movieAPPTesting'

mongo = PyMongo(app)
app_module.mongo = mongo


class AppTestCase(unittest.TestCase):
    """Clean the DB"""
    def setUp(self):
        self.client = app.test_client()
        with app.app_context():
            mongo.db.users.delete_many({})
            mongo.db.recipes.delete_many({})


class AppTests(AppTestCase):
    """Test Home page loading"""
    def test_index(self):
        res = self.client.get('/')
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'Movies' in data

    def test_recipes(self):
        """Test movie list page loading"""
        res = self.client.get('/recipes')
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'features' in data

    def test_register_mismatch_passwords(self):
        """Check mismatched passwords on the registration form, expecting mismatch message"""
        res = self.client.post('/register', data=dict(
            username='fred',
            password='joijqwdoijqwoid',
            password2='qoijwdoiqwjdoiqwd',
            email='fred@aol.com',
        ))
        data = res.data.decode('utf-8')
        assert 'Passwords must match' in data

    def test_register_duplicate_username(self):
        """Check entering a username that is already used returns username is already taken message"""
        res = self.client.post('/register', follow_redirects=True, data=dict(
            username='fred',
            password='asdfasdfasdf',
            password2='asdfasdfasdf',
            email='fred@aol.com',
        ))
        data = res.data.decode('utf-8')
        assert ' Movies' in data
        res = self.client.post('/register', follow_redirects=True, data=dict(
            username='fred',
            password='asdfasdfasdf',
            password2='asdfasdfasdf',
            email='fred@aol.com',
        ))
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'that username is already taken' in data

    def test_register_successful(self):
        """Check valid registration redirects to index page"""
        res = self.client.post('/register', follow_redirects=True, data=dict(
            username='freddie',
            password='asdfasdfasdf',
            password2='asdfasdfasdf',
            email='freddie@aol.com',
        ))
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'A Glut of Movies' in data


class LoggedInTests(AppTestCase):
    """Separate class to clean DB with no cross referencing"""
    def setUp(self):
        """
        Clean the DB, add new user and movie and check user and new movie
        shows on home after redirect
        """
        super().setUp()
        res = self.client.post('/register', follow_redirects=True, data=dict(
            username='fred3',
            password='asdfasdfasdf',
            password2='asdfasdfasdf',
            email='fred3@aol.com',
        ))
        res = self.client.post('/create_movie', follow_redirects=True, data={
            'title': 'Mac and cheese',
            'short_description': 'Get this mac and cheese',
            'ingredients': '8 spring onions',
            'method': 'Put all the ingredients',
            'tags': 'cheese, slow',
            'image': 'some image link'
        })
        data = res.data.decode('utf-8')
        assert 'fred3' in data
        assert 'Mac and cheese'

    def test_create_movie(self):
        """Create movie and check new movie shows after redirect"""
        res = self.client.post('/create_movie', follow_redirects=True, data={
            'title': 'Slow - cooker vegan bean chilli',
            'short_description': 'Get this vegan',
            'ingredients': '8 spring onions',
            'method': 'Put all the ingredients',
            'tags': 'vegan, slow',
            'image': 'some image link'
        })
        data = res.data.decode('utf-8')
        assert 'vegan' in data

    def test_movie_page(self):
        """Find Movie and go to it's movie page"""
        res = self.client.get('/movies')
        # use regular expression to find Object id of movie
        ids = re.findall(r'href="/movie/(\w+)"', res.data.decode("utf8"))
        # check we have something
        assert len(ids) > 0
        # to go that movie page using extracted id
        res = self.client.get('/recipe/{}'.format(ids[0]))
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'Mac and cheese' in data

    def test_edit_movie(self):
        """Edit movie and check redirect to home page"""
        res = self.client.get('/movies')
        ids = re.findall(r'href="/movie/(\w+)"', res.data.decode("utf8"))
        assert len(ids) > 0
        res = self.client.get('/edit_movie/{}'.format(ids[0]))
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'Mac and cheese' in data
        res = self.client.post('/edit_movie/'.format(ids[0]), follow_redirects=True, data={
            'title': 'Mac and cheese',
            'short_description': 'Get this maccy and cheese',
            'ingredients': '8 blocks of cheddar',
            'method': 'Put all the ingredients',
            'tags': 'cheese, slow',
            'image': 'some image link'
        })
        assert res.status == '200 OK'

    def test_delete_movie(self):
        """Delete movie and check movie is not present after redirect"""
        res = self.client.get('/movies')
        # use regular expression to find Object id of movie
        ids = re.findall(r'href="/movie/(\w+)"', res.data.decode("utf-8"))
        assert len(ids) > 0
        # togo that delete movie page using extracted id
        res = self.client.post('/delete_movie/{}'.format(ids[0]), follow_redirects=True)
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'Birdbox' not in data
