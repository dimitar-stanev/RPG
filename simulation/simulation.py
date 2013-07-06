import sqlite3 as lite
import sys
from random import randint


class Character_class_controller:
    def return_class_and_weapon(self, num):
        if num == 1:
            return ('warrior', 1, 7, 3, 3, 300)
        elif num == 2:
            return ('mage', 2, 3, 4, 6, 220)
        elif num == 3:
            return ('rogue', 3, 4, 4, 6, 260)


class Creature_controller:
    name = None
    armor = 0
    luck = 0
    damage = 0
    level = 0
    hp = 0

    def __init__(self, name, damage, armor, luck, level, hp):
        self.name = name
        self.damage = damage
        self.armor = armor
        self.luck = luck
        self.level = level
        self.hp = hp

    def item_dropped(self):
        return randint(1, 10)

    def deal_hit(self):
        return self.damage * self.luck + randint(0, 20)

    def receive_hit(self, damage_done):
        return self.armor * self.luck + self.level*5 - damage_done


class Character_controller:
    name = None
    level = 1
    strength_modifier = 1
    intellect_modifier = 1
    agility_modifier = 1
    classname = None
    strength = None
    agility = None
    intellect = None
    weapon_impact = 0
    armor_impact = 0
    hp = 0
    char_class = 0

    def __init__(self, name, char_class, weapon_impact, armor_impact):

        self.weapon_impact = weapon_impact
        self.armor_impact = armor_impact
        self.char_class = char_class
        self.name = name
        level = 1
        strength_modifier = 1
        intellect_modifier = 1
        agility_modifier = 1
        classname = None

        ccc = Character_class_controller()
        chars_class = ccc.return_class_and_weapon(self.char_class)

        self.classname = chars_class[0]
        self.strength = chars_class[2]
        self.agility = chars_class[3]
        self.intellect = chars_class[4]

        if (chars_class[1] == 1):
            strength_modifier = 1.5
        elif(chars_class[1] == 2):
            intellect_modifier = 1.4
        elif(chars_class[1] == 3):
            agility_modifier = 1.35        

        self.strength += level * 2 * strength_modifier
        self.agility += level * 2 * agility_modifier
        self.intellect += level * 2 * intellect_modifier
        self.hp = chars_class[5] + self.strength * 2
        self.print_info()

    def print_info(self):
        print("This character is a ", self.classname)
        print("His name is :", self.name)
        print("His attributes are : ")
        print("strength : ", self.strength)
        print("agility : ", self.agility)
        print("intellect : ", self.intellect)

    def deal_hit(self):
        ccc = Character_class_controller()
        chars_class = ccc.return_class_and_weapon(self.char_class)
        if self.classname == 'warrior':
            return self.strength*3 + self.weapon_impact
        elif self.classname == 'mage':
            return self.intellect*4 + self.weapon_impact
        elif self.classname == 'rogue':
            return self.agility * 3.5 + self.weapon_impact + randint(1, 10)

    def receive_hit(self, damage):
        ccc = Character_class_controller()
        chars_class = ccc.return_class_and_weapon(self.char_class)
        if self.classname == 'warrior':
            return 6  * self.armor_impact + 10 - damage
        elif self.classname == 'mage':
            return 3 * self.armor_impact - damage
        elif self.classname == 'rogue':
            return self.armor_impact * 4 + randint(1, 10) - damage


class Simulator:

    test_character = None
    test_creature = None
    
    def run_simulation(self):
        self.test_character = Character_controller('Todor', 1, 6, 8)
        self.test_creature = Creature_controller('Troll', 12, 4, 2, 2, 200)
    
    def simulate_battle(self, player, creature):
        while True:
            damage_by_player = player.deal_hit()
            damage_by_creature = creature.deal_hit()
            creature.hp += creature.receive_hit(damage_by_player)
            player.hp += player.receive_hit(damage_by_creature)

            if creature.hp <= 0:
                print('\n',
'                                                 ,-.\n',
'       ___,---.__          /\'|`\          __,---,___\n',
'    ,-\'    \`    `-.____,-\'  |  `-.____,-\'    //    `-.\n',
'  ,\'        |           ~\'\     /`~           |        `.\n',
' /      ___//              `. ,\'          ,  , \___      \\\n',
'|    ,-\'   `-.__   _         |        ,    __,-\'   `-.    |\n',
'|   /          /\_  `   .    |    ,      _/\          \   |\n',
'\  |           \ \`-.___ \   |   / ___,-\'/ /           |  /\n',
' \  \           | `._   `\\  |  //\'   _,\' |           /  /\n',
'  `-.\         /\'  _ `---\'\' , . ``---\' _  `\         /,-\n',
'     ``       /     \    ,=\'/ \`=.    /     \       \'\'\n',
'             |__   /|\_,--.,-.--,--._/|\   __|\n',
'             /  `./  \\`\ |  |  | /,//\' \,\'  \\\n',
'            /   /     ||--+--|--+-/-|     \   \\\n',
'           |   |     /\'\_\_\ | /_/_/`\     |   |\n',
'            \   \__, \_     `~\'     _/ .__/   /\n',
'             `-._,-\'   `-._______,-\'   `-._,-\n',
'                    \n')
                print("Creature is dead !")
                print("It has dropped a :", creature.item_dropped())               # Тук трябва да връща ID на предмет от базата !
                break

            elif player.hp <= 0:
                print("Player has died !")
                break

            else:
                print("Player's hp is :", player.hp)
                print("Creature's hp is :", creature.hp)

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

    sim = Simulator()
    sim.run_simulation()

    print("After that, the data is put into the database !")

    print("We created a character and a creature !")

    sim.simulate_battle(sim.test_character, sim.test_creature)


    # cur.execute('INSERT INTO rpg_game_character VALUES(\'1\', \'' + test_character.name + '\'')')
