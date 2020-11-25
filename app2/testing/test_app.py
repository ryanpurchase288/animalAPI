from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestAnimals(TestBase):
    def test_animal(self):
        animals = [b'cat', b'dog', b'cow', b'duck']
        response = self.client.get(url_for('animal_name'))
        self.assertIn(response.data, animals)

    def test_noise_duck(self):
        response =self.client.post(
            url_for('animal_noise'),
            data='duck',
        
        )
        self.assertIn(b'quack', response.data)
    def test_noise_cow(self):
        response =self.client.post(
            url_for('animal_noise'),
            data='cow',
            
        )
        self.assertIn(b'moo', response.data)  
    def test_noise_dog(self):
        response =self.client.post(
            url_for('animal_noise'),
            data='dog',
            
        )
        self.assertIn(b'woof', response.data)
    def test_noise_cat(self):
        response =self.client.post(
            url_for('animal_noise'),
            data='cat'
           
        )
        self.assertIn(b'meow', response.data)  