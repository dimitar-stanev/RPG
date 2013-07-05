from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image

class Character(models.Model):
    character_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False)
    character_class = models.PositiveIntegerField(max_length=1)
    level = models.PositiveIntegerField()
    created_date = models.DateTimeField('date created')
    avatar = models.ImageField(upload_to='/avatars/')
    items_owned_ids = models.PositiveIntegerField(max_length = 3)
    owner = models.ForeignKey(User)

class Character_class(models.Model):
	class_identifier_id = models.PositiveIntegerField(max_length=1, primary_key=True)
	starting_strength = models.PositiveIntegerField()
	starting_agility = models.PositiveIntegerField()
	starting_intellect = models.PositiveIntegerField()
	starting_weapon_id = models.PositiveIntegerField(max_length=2)

class Item(models.Model):
	item_id = models.AutoField(primary_key=True)
	item_type = models.PositiveIntegerField(max_length=1,null=False)
	item_cost = models.PositiveIntegerField(max_length=5,null=True)
	item_impact = models.PositiveIntegerField(max_length=3, null=False)
	item_bonus_stats = models.PositiveIntegerField(max_length=1)
	item_bonus = models.PositiveIntegerField(max_length=3)

class Creature(models.Model):
	creature_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=64)
	creature_damage = models.PositiveIntegerField(max_length=3)
	creature_armor = models.PositiveIntegerField(max_length=3)
	creature_luck = models.PositiveIntegerField(max_length = 1)
	items_dropped_ids = models.PositiveIntegerField(max_length=2)
