##########################################################
# DO NOT DISTRIBUTE ; DO NOT REPRODUCE ; DO NOT SELL   ###
# COPYRIGHT 2020 RAPHAEL ZOEGA CALI GOMES              ###
# ALL RIGHT RESERVED                                   ###
##########################################################
# Coded in Python 3.8.0 ####
#####################################
# Needed for the game to function. ##
#####################################

import cmd
import textwrap
import sys
import os
import time
import random
import game_functionality
import game_interactivity
import title
import maps
import combat
import inventory_file


#### Player Setup ####
class playerFunction:
	def __init__(self):
		self.name = ''
		self.job = ''
		self.attribute = ''
		self.hp = 0
		self.mp = 0
		self.frc = 0
		self.dex = 0
		self.con = 0
		self.intl = 0
		self.status_effects = []
		self.location = 'quiet hills'
		self.game_over = False
myPlayer = playerFunction()


#### Class (job) system ####
fighter = {
	'job': 'fighter',
	'hp': 100,
	'mp': 10,
	'frc': 30,
	'dex': 5,
	'con': 10,
	'intl': 15,
	}
mage = {
	'job': 'mage',
	'hp': 50,
	'mp': 150,
	'frc': 0,
	'dex': 5,
	'con': 5,
	'intl': 30,
	}

rogue = {
	'job': 'rogue',
	'hp': 70,
	'mp': 10,
	'frc': 20,
	'dex': 15,
	'con': 10,
	'intl': 15,
	}

priest = {
	'job': 'priest',
	'hp': 150,
	'mp': 60,
	'frc': 5,
	'dex': 0,
	'con': 15,
	'intl': 15,
	}

#### Attributes system ####
strong = {
	'attribute': 'strong',
	'hp': 50,
	'mp': 10,
	'frc': 30,
	'dex': 10,
	'con': 10,
	'intl': 5,
	}

smart = {
	'attribute': 'smart',
	'hp': 20,
	'mp': 50,
	'frc': 5,
	'dex': 15,
	'con': 10,
	'intl': 30,
	}

tank = {
	'attribute': 'tank',
	'hp': 100,
	'mp': 0,
	'frc': 10,
	'dex': 5,
	'con': 15,
	'intl': 10,
	}

balanced = {
	'attribute': 'balanced',
	'hp': 30,
	'mp': 30,
	'frc': 10,
	'dex': 15,
	'con': 10,
	'intl': 15,
	}

#### CHECK STATS FUNCTION ####
def stats_check():
	print('#' * 30 + '\n')
	print(myPlayer.name.upper() + '\n' + ' Job: ' + myPlayer.job + '	Attributes: ' + myPlayer.attribute)
	print(' HP =', myPlayer.hp, '	MP =', myPlayer.mp, '\n', 'FRC =', myPlayer.frc, '	DEX =', myPlayer.dex, '\n', 'CON =', myPlayer.con, '	INTL =', myPlayer.intl)
	for i in range(inventory_file.inventory.current_storage):
			print(inventory_file.inventory.items[i].name + ' ')
	print(' Current storage usage:', inventory_file.inventory.current_storage, '/', inventory_file.inventory.max_storage)
	print('\n' + '#' * 30 + '\n')
	game_interactivity.prompt()