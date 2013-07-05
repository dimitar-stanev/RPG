"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.utils import timezone
from django.test import TestCase
from rpg_game.models import *

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class TestingCharacters(TestCase):

	test_character = Character()

    def test_creating_character(self):
    	"""Tests creation of character"""
    	self.assertEqual(test_character.__dict__, '{\'level\': None, \'name\': \'' + 
    		'\', \'created_date\': None, \'owner_id\': None, \'character_class\': None, ' +
    		'\'items_owned_ids\': None, \'avatar\': \'\', \'_state\': <django.db.models.base.ModelState object at 0x0000000003CA1748>, ' +
    		'\'character_id\': None}')

    def test_modifying_properties(TestCase):
    	test_character.name = 'Pesho'
    	test_character.level = 2
    	test_character.owner_id = None
    	test_character.items_owned_ids = 1
    	test_character.character_class = 1
    	test_character.avatar = None
    	test_character.created_date = timezone.now()
    	test_character.items_owned_ids = 234
    	test_character.owner_id = 0
    	self.assertEqual(test_character.name, 'Pesho')

    def test_saving_character(TestCase):
    	self.assertEqual(test_character.save(), '')
