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
import player
import game_functionality
import title
import maps
import combat
import inventory_file
import npcs

#### Game Interactivity ####
def print_location():
	print('\n' + ('-' * (4 + len(player.myPlayer.location))))
	print('- ' + player.myPlayer.location.upper() + ' -')
	print('\n' + ('-' * (4 + len(player.myPlayer.location))))
	print('# ' + maps.zonemap[player.myPlayer.location][maps.DESCRIPTION] + ' #')
	print('\n' + ('-' * (4 + len(player.myPlayer.location))))

def prompt():
	print('\n' + ('=' * 27))
	print(" What would you like to do?")

	action = input("> ")
	print("")
	acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'interact', 'look', 'map', 'help', 'inventory', 'stats']

	while action.lower() not in acceptable_actions:
		print(" Uknown action, try again. \n")
		action = input("> ")
		print("")

	if action.lower() == 'quit':
		sys.exit()

	elif action.lower() in ['move', 'go', 'travel', 'walk']:
		player_move()

	elif action.lower() in ['examine', 'interact', 'look']:
		player_examine()

	elif action.lower() == 'map':
		open_map()

	elif action.lower() == 'inventory':
		inventory_file.inventory_menu()

	elif action.lower() == 'help':
		tutorial_function()

	elif action.lower() == 'stats':
		player.stats_check()


#### MOVEMENT FUNCTIONS ####
def player_move():
	dest = input(" Where would you you like to move to?\n")
	print('\n' + ('=' * 27))


	if dest.lower() in ['up', 'north']:
		destination = maps.zonemap[player.myPlayer.location][maps.UP]
		movement_handler(destination)

	elif dest.lower() in ['left', 'west']:
		destination = maps.zonemap[player.myPlayer.location][maps.LEFT]
		movement_handler(destination)

	elif dest.lower() in ['right', 'east']:
		destination = maps.zonemap[player.myPlayer.location][maps.RIGHT]
		movement_handler(destination)

	elif dest.lower() in ['down', 'south']:
		destination = maps.zonemap[player.myPlayer.location][maps.DOWN]
		movement_handler(destination)

	else:
		print("\n Uknown action")
		prompt()


def movement_handler(destination):
	if destination == '':
		notice = "\n You can't move in this direction \n"
		for character in notice:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.04)
		prompt()
	else:
		os.system('cls')
		print("\n" + " You have moved to " + destination + ".")
		player.myPlayer.location = destination
		print_location()
		combat.encounter_medium()
		prompt()

#### EXAMINATION FUNTION ####
def player_examine():
	print('\n' + ('=' * 27) + '\n')
	print(maps.zonemap[player.myPlayer.location][maps.EXAMINATION])
	npcs.check_location(player.myPlayer.location)
	prompt()

#### OPEN MAP FUNCTION ####
def open_map():
	map_file = open('map.txt', 'r')
	print(map_file.read())
	map_file.close()
	prompt()

#### TUTORIAL FUNCTION ####
def tutorial_function():
	notice1 = ""
	for character in notice1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	reader = open("tutorial.txt", "r")
	print(reader.read())
	reader.close()
	prompt()