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
import pygame
import player
import game_functionality
import game_interactivity
import title
import maps
import inventory_file
import npcs

player_damage = 0
enemy_damage = 0
mana_regen = 0

# SETTING UP MUSIC WITH PYGAME MIXER
pygame.init() # Initialize Pygame

musicPlayerIcon = pygame.image.load('musicPlayerIcon.png') # Set up pygame window as MUSIC PLAYER
pygame.display.set_mode((250, 50))
pygame.display.set_caption('MUSIC PLAYER')
pygame.display.set_icon(musicPlayerIcon)

combat_music = pygame.mixer.Sound('Music/Combat.wav')
victory_music = pygame.mixer.Sound('Music/Victory.wav')
SWORDTAKE = pygame.mixer.Sound('SFX/SWORDTAKE.wav')
SWORDHIT = pygame.mixer.Sound('SFX/SWORDHIT.wav')
channel0 = pygame.mixer.Channel(0)
channel0.set_volume(0.3)
channel1 = pygame.mixer.Channel(1)

#### ENEMY CLASSES ####
class attackerFunction:
	def __init__(self):
		self.type = 'humanoid'
		self.hp = 100
		self.mp = 20
		self.frc = 60
		self.dex = 12
		self.con = 10
		self.intl = 5
common_attacker = attackerFunction()

#### RANDOM GENERATOR ####
def encounter_medium():
	encounter = random.randint(1,100)

	if encounter <= 30:
		channel0.play(combat_music)
		channel1.play(SWORDTAKE)
		os.system('cls')
		notice1 = random_fight_text() + '\n'

		for character in notice1:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.04)

		common_attacker.hp += (100 - common_attacker.hp)

		combat_screen()

#### COMBAT SCREEN ####
def combat_screen():
	print("=" * 30)
	print(" Current health points:", player.myPlayer.hp, '\n')
	notice1 = " What will you do? \n"
	notice2 = "{You can fight, heal or flee} \n"
	for character in notice1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.03)
	for character in notice2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.03)

	check = input("> ")
	print("")
	acceptable_inputs = ['strike', 'attack', 'fight', 'heal', 'potion', 'flee', 'run', 'use', 'stats']

	if check.lower() in acceptable_inputs:
		combat_function(check)

	else:
		print("\n Enter a valid action\n")
		combat_screen()


#### COMBAT FUNCTION ####
def combat_function(check):
	if check.lower() in ['strike', 'attack', 'fight']:
		fight_function()

	elif check.lower() in ['heal', 'potion']:
		heal_function()

	elif check.lower() in ['flee', 'run']:
		flee_function()

	elif check.lower() == 'use':
		use_function()

	elif check.lower() == 'stats':
		player.stats_check()
		combat_screen()

	else:
		print("\nEnter a valid action\n")
		combat_screen()

#### FIGHT FUNCTIONs ####
def fight_function():
	notice1 = "\n Will you make a MELEE attack or a MAGIC attack? \n"
	for character in notice1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.03)
	
	check = input("> ")
	acceptable_inputs = ['melee', 'magic']
	while check.lower() not in acceptable_inputs:
		print("\n Unknown action\n")
		check = input("> ")

	if check.lower() == 'melee':
		melee_strike()
				
	if check.lower() == 'magic':
		magic_strike()



# MAGIC ATTACK FUNCTION #
def magic_strike():
	player_damage = player.myPlayer.intl - common_attacker.intl
	enemy_damage = common_attacker.frc - player.myPlayer.con
	player_speed = player.myPlayer.dex
	enemy_speed = common_attacker.dex

	if player.myPlayer.mp <= 0:
		notice2 = "\n You have ran out of mana, and can't cast more magic spells."
		for character in notice2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		combat_function()
	elif player.myPlayer.mp > 0:
		player.myPlayer.mp -= 10

		if player_damage <= 0:
			player_damage = 0
			notice2 = "\n Your attack barely grazes your target. \n"
			for character in notice2:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.03)

			player.myPlayer.hp -= enemy_damage
			print(player.myPlayer.hp)

			if player.myPlayer.hp <= 0:
				player.myPlayer.game_over = True
				game_functionality.main_game_loop()
			else:
				combat_screen()

		elif player_damage > 0:
			if player.myPlayer.dex >= common_attacker.dex:
				common_attacker.hp -= player_damage

				if common_attacker.hp <= 0:
					print("")
					os.system('cls')
					victory_screen("defeated")
				else:
					player.myPlayer.hp -= enemy_damage
					if player.myPlayer.hp <= 0:
						player.myPlayer.game_over = True
						os.system('cls')
						game_functionality.main_game_loop()
					else:
						print(player.myPlayer.hp)
						combat_screen()

			elif player.myPlayer.dex < common_attacker.dex:
				player.myPlayer.hp -= enemy_damage

				if player.myPlayer.hp <= 0:
					player.myPlayer.game_over = True
					game_functionality.main_game_loop()

				else:
					common_attacker.hp -= player_damage
					if common_attacker.hp <= 0:
						print("")
						os.system('cls')
						victory_screen("defeated")
					else:
						print(player.myPlayer.hp)
						combat_screen()

# MELEE ATTACK FUNCTION #
def melee_strike():
	player_damage = player.myPlayer.frc - common_attacker.con
	enemy_damage = common_attacker.frc - player.myPlayer.con
	player_speed = player.myPlayer.dex
	enemy_speed = common_attacker.dex

	if player_damage <= 0:
		player_damage = 0
		notice2 = "\n Your attack barely grazes your target. \n"
		for character in notice2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)

		player.myPlayer.hp -= enemy_damage
		print(player.myPlayer.hp)

		if player.myPlayer.hp <= 0:
			player.myPlayer.game_over = True
			os.system('cls')
			game_functionality.main_game_loop()
		else:
			combat_screen()

	else:
		if player.myPlayer.dex >= common_attacker.dex:
			common_attacker.hp -= player_damage
			channel1.play(SWORDHIT)

			if common_attacker.hp <= 0:
				print("")
				os.system('cls')
				victory_screen("defeated")
			else:
				player.myPlayer.hp -= enemy_damage
				if player.myPlayer.hp <= 0:
					player.myPlayer.game_over = True
					os.system('cls')
					game_functionality.main_game_loop()
				else:
					print(player.myPlayer.hp)
					combat_screen()
			print(player.myPlayer.hp)

		elif player.myPlayer.dex < common_attacker.dex:
			player.myPlayer.hp -= enemy_damage

			if player.myPlayer.hp <= 0:
				player.myPlayer.game_over = True
				os.system('cls')
				game_functionality.main_game_loop()

			else:
				common_attacker.hp -= player_damage
				channel1.play(SWORDHIT)
				if common_attacker.hp <= 0:
					print("")
					os.system('cls')
					victory_screen("defeated")
				else:
					print(player.myPlayer.hp)
					combat_screen()


#### FLEE FUNCTION ####
def flee_function():
	player_speed = player.myPlayer.dex
	enemy_speed = common_attacker.dex
	random_number1 = random.randint(1,20)
	random_number2 = random.randint(1,20)
	player_escape = player_speed + random_number1
	enemy_escape = enemy_speed + random_number2

	if player_escape >= enemy_escape:
		victory_screen("escaped")

	else:
		notice1 = "\n You couldn't escape from the fight. \n"
		for character in notice1:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.02)
		combat_screen()


#### HEALING FUNCTION ####
def heal_function():
	if inventory_file.inventory.current_storage == 0:
		print("You don't have any remaining potions.\n")
	else:
		for i in range(inventory_file.inventory.current_storage):
			if inventory_file.inventory.items[i].name == 'potion':
				player.myPlayer.hp += 20
				inventory_file.inventory.items.remove(inventory_file.inventory.items[i])
				inventory_file.inventory.current_storage -= 1
				break
	combat_screen()

#### VITORY SCREEN FUNCTION ####
def victory_screen(func):
	os.system('cls')
	channel0.play(victory_music)

	notice1 = " You've successfuly " + func + " the enemy. \n"
	for character in notice1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	print("Galileo Asteros: ")
	if func == 'escaped':
		text = aster_random_flee()
	else:
		text = aster_random_win()
	for character in text:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	time.sleep(2)
	game_interactivity.print_location()
	game_functionality.main_game_loop()


#### RANDOM TEXT GENERATORS ####
def random_fight_text():
	text_selector = random.randint(1,5)

	if text_selector == 1:
		text = " An enemy approaches you menacingly. \n"
		return text

	elif text_selector == 2:
		text = " An adversary get closer and closer, preparing a strike. \n"
		return text

	elif text_selector == 3:
		text = " Facing you from a distance, an enemy lurks waiting to strike. \n "
		return text

	elif text_selector == 4:
		text = " An enemy approaches; you cross your sights; that's the gesture of a fight. \n"
		return text

	elif text_selector == 5:
		text = " An enemy is near; it's fight or flee now. \n"
		return text

#### RANDOM G. ASTER VICTORY TEXT GENERATOR ####
def aster_random_win():
	text_selector = random.randint(1,20)

	if text_selector >= 1 or text_selector <= 4:
		text = " Well, that certainly was a close one. \n"
		return text

	elif text_selector >= 5 or text_selector <= 9:
		text = " Oh, wonderfully done. May it never happen again. \n"
		return text

	elif text_selector >= 10 or text_selector <= 14:
		text = " That was a magnificent skirmish.\n Thou art a profoundly competent brawler " + player.myPlayer.name + ". \n "
		return text

	elif text_selector >= 15 or text_selector <= 19:
		text = " I could, indeed, have helped, but thou was handling\n it so effectively I wasn't inclined to interrupt. \n"
		return text

	elif text_selector == 20:
		text = " Tis wound? Tis but a scratch. \n"
		return text

def aster_random_flee():
	text_selector = random.randint(1,20)

	if text_selector >= 1 or text_selector <= 4:
		text = " Well, that certainly was a close one. \n"
		return text

	elif text_selector >= 5 or text_selector <= 9:
		text = " Oh, wonderfully done. May it never happen again. \n"
		return text

	elif text_selector >= 10 or text_selector <= 14:
		text = " We barely managed to flee.\n But we did. That's the important bit. \n" + player.myPlayer.name + ". \n "
		return text

	elif text_selector >= 15 or text_selector <= 19:
		text = " He was too weak for us anyway. \n"
		return text

	elif text_selector == 20:
		text = " Why, are fleeing?\n Just go back and fight like a man. \n"
		return text