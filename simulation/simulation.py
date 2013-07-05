import sqlite3 as lite
import sys

class Character_class_controller:
	def return_class(self, num):
		if num == 1:
			return 'warrior'
		elif num == 2:
			return "mage"
		elif num == 3:
			return "rogue"

class Character_controller:
	def __init__(self, name, char_class):
		level = 1
		strength_modifier = 0
		intellect_modifier = 0
		agility_modifier = 0
		strength = level*2 + strength_modifier
		agility = level*2 + agility_modifier
		intellect = intellect*2 + intellect_modifier

con = lite.connect('C:\\Users\\Dimityr\\Desktop\\University\\Python\\prj\\RPG\\RPG\\model\\database.db')
with con:
    
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()

    cur.execute('SELECT * from rpg_game_character WHERE name=\'Pesho\'')
    char = cur.fetchone()

    print(char[1])

    print ("SQLite version:", data, '\n' , char)

    print("Here users input their character info and choice : ")

    # cur.execute('INSERT INTO rpg_game_character')