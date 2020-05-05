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
import game_interactivity
import title
import maps
import combat

global_item_list = {}

class GlobalItemClass:
	def __init__(self, name, description, location, use):
		self.name = name
		self.description = description
		self.location = location
		self.use = use

potion = GlobalItemClass('potion', 'heals you by 20 hp', '', 'heal')
mp_potion = GlobalItemClass('mp potion', 'restores 10 magic points', '', 'mp')
runic_mark = GlobalItemClass('runic mark', 'a strange stone with weird runes carved into it', 'City of Pandora', 'nothing' )

#### INVENTORY CLASS ####
class Inventory:
	def __init__(self):
		self.max_storage = 10
		self.current_storage = 0
		self.items = []
inventory = Inventory()

#### INVENTORY MENU FUNCTION ####
def inventory_menu():
	print('#' * 30 + '\n')
	notice1 = " You open your backpack. \n"
	for character in notice1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.03)
	if inventory.current_storage == 0:
		notice2 = "\n It is completely empty. \n"
		for character in notice2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		print('\n' + '#' * 30 + '\n')
		game_interactivity.prompt()

	else:
		notice2 = "\n The backpack is full of items. \n"
		notice3 = " What would you like to do? \n"
		for character in notice2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)

		print("- - - - -")
		for i in range(inventory.current_storage):
			print(inventory.items[i].name +'\n')
		print("- - - - -")

		for character in notice3:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)

		check = input("> ")
		acceptable_inputs = ['remove', 'inspect', 'quit', 'use']
		while check not in acceptable_inputs:
			print("Enter a valid input.")
			check = input("> ")

		if check.lower() == 'remove':
			item_remove()

		elif check.lower() == 'inspect':
			item_inspector()

		elif check.lower() == 'quit':
			print('#' * 30 + '\n')
			game_interactivity.prompt()

		elif check.lower() == 'use':
			use_item()

"""

NEEDS REWORK

#### FUNCTION FOR GETTING ITEMS ####
def get_item(item):
	if inventory.current_storage == inventory.max_storage:
		notice1 = " Your inventory is full. "
		for character in notice1:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)

		print(" These are your current items:", inventory.items)
	elif item in global_item_dictionary:
		invenory.append(item.lower())
		invontory.current_storage += 1

	else:
		notice1 = " This item does not exist. "
		for character in notice1:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)

#### FUNCTION FOR REMOVING ITEMS FROM INVENTORY ####
def item_remove():
	item = ''

	notice1 = " What item do you want to remove? "
	for character in notice1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.03)

	item_holder = input("> ")

	if item_holder.lower() in inventory.items:
		notice2 = " Are you sure you want to remove " + item_holder.lower() + " from your inventory? "
		for character in notice2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)

		check = input("> ")
		acceptable_inputs = ['no', 'yes']

		if check.lower() in acceptable_inputs:
			if check.lower() == 'yes':
				inventory.items.remove(item_holder.lower())
				inventory.current_storage -= 1
				print(" These are your current items:", inventory.items)
				inventory_menu()
			else:
				inventory_menu()
"""				

#### FUNCTION FOR INSPECTING ITEMS ####
def item_inspector():

	notice1 = "\n What item do you want to inspect? \n"
	for character in notice1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.03)

	item_holder = input("> ")
	lower_holder = item_holder.lower()

	for i in range(inventory.current_storage):
		if inventory.items[i].name == lower_holder:
			notice2 = "\n" + inventory.items[i].description + "\n"
			notice3 = " It was found in: " + inventory.items[i].location + "\n"
			for character in notice2:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.03)
			for character in notice3:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.03)
			break
	inventory_menu()

#### FUNCTION FOR USING ITEMS ####
def use_item():
	notice1 = "\n What item do you want to use? \n"
	for character in notice1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.03)

	item_holder = input("> ")
	lower_holder = item_holder.lower()

	for i in range(inventory.current_storage):
		if inventory.items[i].name == lower_holder:

			if inventory.items[i].use == 'heal':
				player.myPlayer.hp += 20
				inventory.items.remove(inventory.items[i])
				inventory.current_storage -= 1

				notice2 = " Healed 20 health points. \n"
				for character in notice2:
					sys.stdout.write(character)
					sys.stdout.flush()
					time.sleep(0.03)

			elif inventory.items[i].use == 'mp':
				player.myPlayer.hp += 10
				inventory.items.remove(inventory.items[i])
				inventory.current_storage -= 1

				notice2 = " Restored 10 magic points. \n"
				for character in notice2:
					sys.stdout.write(character)
					sys.stdout.flush()
					time.sleep(0.03)

			elif inventory.items[i].use == 'nothing':
				notice2 = " This item doesn't do anything \n"
				for character in notice2:
					sys.stdout.write(character)
					sys.stdout.flush()
					time.sleep(0.03)

			elif inventory.items[i].use == '':
				notice2 = " This item can't be used \n"
				for character in notice2:
					sys.stdout.write(character)
					sys.stdout.flush()
					time.sleep(0.03)
			break

		else:
			notice2 = " You don't have such item. \n"
			for character in notice2:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.03)
			print('-' * 10 + '\n')
	inventory_menu()