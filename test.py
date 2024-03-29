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
app.config['MONGO_URI'] = 'mongodb://localhost:5000/movieAPPTesting'

mongo = PyMongo(app)
app_module.mongo = mongo


class AppTestCase(unittest.TestCase):
    """Clean the DB"""
    def setUp(self):
        self.client = app.test_client()
        with app.app_context():
            mongo.db.users.delete_many({})
            mongo.db.movies.delete_many({})


class AppTests(AppTestCase):
    """Test Home page loading"""
    def test_index(self):
        res = self.client.get('/')
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'Movies' in data

    def test_movies(self):
        """Test movie list page loading"""
        res = self.client.get('/movies')
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'features' in data

    def test_register_mismatch_passwords(self):
        """Check mismatched passwords on the registration form, expecting mismatch message"""
        res = self.client.post('/register', data=dict(
            username='freggie',
            password='joijqwdoijqwoid',
            password2='qoijwdoiqwjdoiqwd',
            email='freggie@gmail.com',
        ))
        data = res.data.decode('utf-8')
        assert 'Passwords must match' in data

    def test_register_duplicate_username(self):
        """Check entering a username that is already used returns username is already taken message"""
        res = self.client.post('/register', follow_redirects=True, data=dict(
            username='freda',
            password='asdfasdfasmu',
            password2='asdfasdfasmu',
            email='freda@gmail.com',
        ))
        data = res.data.decode('utf-8')
        assert ' Movies' in data
        res = self.client.post('/register', follow_redirects=True, data=dict(
            username='freda',
            password='asdfasdfasvq',
            password2='asdfasdfasvq',
            email='freda@gmail.com',
        ))
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'that username is already taken' in data

    def test_register_successful(self):
        """Check valid registration redirects to index page"""
        res = self.client.post('/register', follow_redirects=True, data=dict(
            username='Fremah',
            password='akuaghfad',
            password2='akuaghfad',
            email='fremah@gmail.com',
        ))
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'Movie App' in data


class LoggedInTests(AppTestCase):
    """Separate class to clean DB with no cross referencing"""
    def setUp(self):
        """
        Clean the DB, add new user and movie and check user and new movie
        shows on home after redirect
        """
        super().setUp()
        res = self.client.post('/register', follow_redirects=True, data=dict(
            username='Junior',
            password='joijqwdoijqwoid',
            password2='joijqwdoijqwoid',
            email='jnr1015@gmail.com',
        ))
        res = self.client.post('/create_movie', follow_redirects=True, data={
            'title': 'Magnificient 7',
            'short_description': 'The movie is about holocust took place in Texas in the United States of America',
            'collections': 'Action',
            'image': 'some image link'
        })
        data = res.data.decode('utf-8')
        assert 'Kofy1' in data
        assert 'Magnificient 7'

    def test_create_movie(self):
        """Create movie and check new movie shows after redirect"""
        res = self.client.post('/create_movie', follow_redirects=True, data={
            'title': 'Magnificient 7',
            'short_description': 'The movie is about holocust took place in Texas in the United States of America',
            'collections': 'Action',
            'image': 'some image link'
        })
        data = res.data.decode('utf-8')
        assert 'Magnificient 7' in data

    def test_movie_page(self):
        """Find Movie and go to it's movie page"""
        res = self.client.get('/movies')
        # use regular expression to find Object id of movie
        ids = re.findall(r'href="/movie/(\w+)"', res.data.decode("utf8"))
        # check we have something
        assert len(ids) > 0
        # to go that movie page using extracted id
        res = self.client.get('/movie/{}'.format(ids[0]))
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'Magnificient 7' in data

    def test_edit_movie(self):
        """Edit movie and check redirect to home page"""
        res = self.client.get('/movies')
        ids = re.findall(r'href="/movie/(\w+)"', res.data.decode("utf8"))
        assert len(ids) > 0
        res = self.client.get('/edit_movie/{}'.format(ids[0]))
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'Equalizer' in data
        res = self.client.post('/edit_movie/'.format(ids[0]), follow_redirects=True, data={
            'title': 'Equalizer',
            'short_description': 'This is a movie which talks about an FBI agent who is on the siege to battle crime',
            'collections': 'Action and Sizzling',
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
        assert 'Magnificient 7' not in data
