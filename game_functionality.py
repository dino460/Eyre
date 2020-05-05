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
import game_interactivity
import title
import maps
import combat
import inventory_file

god_mode = False

# SETTING UP MUSIC WITH PYGAME MIXER
pygame.init() # Initialize Pygame

musicPlayerIcon = pygame.image.load('musicPlayerIcon.png') # Set up pygame window as MUSIC PLAYER
pygame.display.set_mode((250, 50))
pygame.display.set_caption('MUSIC PLAYER')
pygame.display.set_icon(musicPlayerIcon)

overworld_music = pygame.mixer.Sound('Music/Overworld.wav')
death_music = pygame.mixer.Sound('Music/Death.wav')
characterMenu_music = pygame.mixer.Sound('Music/CharacterMenu.wav')
GALILEO_A = pygame.mixer.Sound('SFX/GALILEO_A.wav')
channel0 = pygame.mixer.Channel(0)
channel0.set_volume(0.3)
channel1 = pygame.mixer.Channel(1)

#### Game Functionality ####
def main_game_loop():
	while player.myPlayer.game_over == False:
		channel0.play(overworld_music)
		game_interactivity.prompt()
	if player.myPlayer.game_over == True:
		game_over_screen()

def setup_game():
	os.system('cls')
	channel0.play(characterMenu_music, -1)
	
	### Name collecting
	question1 = "\nWould thou inform me of thy honorific again?\n"
	for character in question1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.04)
	player_name = input("> ")

	if player_name.lower() == 'frisk':
		notice1 = "WARNING: This name will make your life hell.\nProceed anyway?\n"
		for character in notice1: 
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.04)
		check = input("> ")
		if check.lower() == 'yes' or check.lower() == 'y':
			player.myPlayer.job = 'murderer'
			player.myPlayer.attribute = 'weak'
			player.myPlayer.hp += 100
			player.myPlayer.mp += 100
			player.myPlayer.frc += 50
			player.myPlayer.dex += 20
			player.myPlayer.con += 30
			player.myPlayer.intl += 30
			inventory_file.inventory.items.append(inventory_file.potion)
			inventory_file.inventory.items.append(inventory_file.potion)
			inventory_file.inventory.current_storage += 2

			player.myPlayer.name = player_name
			starter()
		else:
			setup_game()

	elif player_name.lower() == 'gaster':
		os.system('cls')
		channel0.stop()
		notice = "YOU SHOULDN'T BE HERE"
		for character in notice:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.6)
		sys.exit()

	elif player_name.lower() == 'god':
		notice = "God mode: True\n"
		for character in notice:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.05)

		global god_mode
		god_mode = True
		expendable = input("> ")

		player.myPlayer.job = 'all father'
		player.myPlayer.attribute = 'immortal'
		player.myPlayer.hp += 999999
		player.myPlayer.mp += 999999
		player.myPlayer.frc += 999999
		player.myPlayer.dex += 999999
		player.myPlayer.con += 999999
		player.myPlayer.intl += 999999
		player.myPlayer.name = player_name

		main_game_loop()

	elif player_name.lower() == 'pickle rick':
		notice = "I'M PICKLE RIIIICK!!!"
		for character in notice:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		player.myPlayer.job = 'pickle'
		player.myPlayer.attribute = 'pickle'
		player.myPlayer.hp += 10
		player.myPlayer.mp += 200
		player.myPlayer.frc += 5
		player.myPlayer.dex += 30
		player.myPlayer.con += 55
		player.myPlayer.intl += 105
		player.myPlayer.name = player_name

		starter()

	elif player_name.lower() == 'dio':
		os.system('cls')
		notice = "KONO DIO DA!!!\n"
		for character in notice:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		notice = "ZA WAARRUUDOOOOOO!!!\n"
		for character in notice:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.02)
		time.sleep(3)
		print("1 second has passed")
		time.sleep(1)
		print("2 seconds have passed")
		time.sleep(1)
		noice = "HO? ARE YOU APPROACHING ME. JOOOOJO?\nINSTEAD OF RUNNING AWAY, YOU'RE COMING RIGHT TO ME?"
		for character in notice:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.02)
		time.sleep(3)
		print("3 seconds have passed")
		time.sleep(1)
		print("4 seconds have passed")
		time.sleep(1)
		print("5 seconds have passed")
		time.sleep(1)
		sys.exit()

	elif player_name.lower() == 'ea':
		notice = "You need to buy the expansion pass to use this name."
		for character in notice:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.05)

		expendable = input("> ")
		setup_game()

	elif player_name.lower() == 'quit':
		notice = "Exiting game.\n"
		for character in notice:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.05)
		notice1 = ". . ."
		for character in notice1:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.2)
		time.sleep(1)
		sys.exit()

	else:

		player.myPlayer.name = player_name

		### Class (job) collecting
		question2 = "\nOh, magnificent! And also, what is thy class?\n"
		question2added = "{You can play as a fighter, a mage, a rogue or a priest}\n"
		for character in question2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.04)
		for character in question2added:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.02)

		### Player job stats
		player_job = input("> ")
		valid_jobs = ['fighter', 'mage', 'rogue', 'priest', 'quit']

		if player_job.lower() in valid_jobs:
			player.myPlayer.job = player_job.lower()
			print("\n Thou art a " + player_job.lower())

		while player_job.lower() not in valid_jobs:
			print("\n Please pick a valid job \n")
			player_job = input("> ")

			if player_job.lower() in valid_jobs:
				player.myPlayer.job = player_job.lower()
				print("\n Thou art a " + player_job.lower())

		if player_job.lower() == 'fighter':
			player.myPlayer.job = player.fighter['job']
			player.myPlayer.hp += player.fighter['hp']
			player.myPlayer.mp += player.fighter['mp']
			player.myPlayer.frc += player.fighter['frc']
			player.myPlayer.dex += player.fighter['dex']
			player.myPlayer.con += player.fighter['con']
			player.myPlayer.intl += player.fighter['intl']

		elif player_job.lower() == 'mage':
			player.myPlayer.job = player.mage['job']
			player.myPlayer.hp += player.mage['hp']
			player.myPlayer.mp += player.mage['mp']
			player.myPlayer.frc += player.mage['frc']
			player.myPlayer.dex += player.mage['dex']
			player.myPlayer.con += player.mage['con']
			player.myPlayer.intl += player.mage['intl']

		elif player_job.lower() == 'rogue':
			player.myPlayer.job = player.rogue['job']
			player.myPlayer.hp += player.rogue['hp']
			player.myPlayer.mp += player.rogue['mp']
			player.myPlayer.frc += player.rogue['frc']
			player.myPlayer.dex += player.rogue['dex']
			player.myPlayer.con += player.rogue['con']
			player.myPlayer.intl += player.rogue['intl']

		elif player_job.lower() == 'priest':
			player.myPlayer.job = player.priest['job']
			player.myPlayer.hp += player.priest['hp']
			player.myPlayer.mp += player.priest['mp']
			player.myPlayer.frc += player.priest['frc']
			player.myPlayer.dex += player.priest['dex']
			player.myPlayer.con += player.priest['con']
			player.myPlayer.intl += player.priest['intl']

		elif player_job.lower() == 'quit':
			notice = "Exiting game.\n"
			for character in notice:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.05)
			notice1 = ". . ."
			for character in notice1:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.2)
			time.sleep(1)
			sys.exit()

		print('')

		### Attributes collecting
		question3 = "\nAlso what art thy attributes?\n"
		question3added = "{You can choose between strong, smart, tank and balanced}\n"
		for character in question3:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.04)
		for character in question3added:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.02)

		### Player attributes stats
		player_attributes = input("> ")
		valid_attributes = ['strong', 'smart', 'tank', 'balanced', 'quit']

		if player_attributes.lower() in valid_attributes:
			player.myPlayer.attributes = player_attributes.lower()
			print("\n Thou art " + player_attributes.lower())

		while player_attributes.lower() not in valid_attributes:
			print("\n Please pick a valid attribute \n")
			player_attributes = input("> ")

			if player_attributes.lower() in valid_attributes:
				player.myPlayer.attributes = player_attributes.lower()
				print("\n Thou art " + player_attributes.lower())

		if player_attributes.lower() == 'strong':
			player.myPlayer.attribute = player.strong['attribute']
			player.myPlayer.hp += player.strong['hp']
			player.myPlayer.mp += player.strong['mp']
			player.myPlayer.frc += player.strong['frc']
			player.myPlayer.dex += player.strong['dex']
			player.myPlayer.con += player.strong['con']
			player.myPlayer.intl += player.strong['intl']

		elif player_attributes.lower() == 'smart':
			player.myPlayer.attribute = player.smart['attribute']
			player.myPlayer.hp += player.smart['hp']
			player.myPlayer.mp += player.smart['mp']
			player.myPlayer.frc += player.smart['frc']
			player.myPlayer.dex += player.smart['dex']
			player.myPlayer.con += player.smart['con']
			player.myPlayer.intl += player.smart['intl']

		elif player_attributes.lower() == 'tank':
			player.myPlayer.attribute = player.tank['attribute']
			player.myPlayer.hp += player.tank['hp']
			player.myPlayer.mp += player.tank['mp']
			player.myPlayer.frc += player.tank['frc']
			player.myPlayer.dex += player.tank['dex']
			player.myPlayer.con += player.tank['con']
			player.myPlayer.intl += player.tank['intl']

		elif player_attributes.lower() == 'balanced':
			player.myPlayer.attribute = player.balanced['attribute']
			player.myPlayer.hp += player.balanced['hp']
			player.myPlayer.mp += player.balanced['mp']
			player.myPlayer.frc += player.balanced['frc']
			player.myPlayer.dex += player.balanced['dex']
			player.myPlayer.con += player.balanced['con']
			player.myPlayer.intl += player.balanced['intl']

		elif player_attributes.lower() == 'quit':
			notice = "Exiting game.\n"
			for character in notice:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.05)
			notice1 = ". . ."
			for character in notice1:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.2)
			time.sleep(1)
			sys.exit()


		print('')

		### Introduction
		question3 = "Welcome, " + player_name + ", the " + player_attributes + " " + player_job + ".\n"
		for character in question3:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.05)

		start_announce = "May thy adventure commence.\n"
		for character in start_announce:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.05)

		expendable = input("> ")
		if expendable.lower() == 'quit':
			notice = "Exiting game.\n"
			for character in notice:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.05)
			notice1 = ". . ."
			for character in notice1:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.2)
			time.sleep(1)
			sys.exit()
		else:
			starter()

def starter():
	channel0.stop()
	os.system('cls')

	intro1 = "\nYou can feel the airship touching the ground. Galileo Asteros\n taps gently in your left shoulder and, supposedly, extends\n his arm to guide you. You find it right where it should be,\n and let yourself be guided by your slim, but rather strong, companion.\n"
	intro2 = "\n Galileo Asteros:\n  Off we go. Mind thy steps, my dear friend.\n"
	intro3 = "\nYou hear the engines being shut down, the captain giving the\n order for disembark. You leave this marvel of engineering besides\n Aster, both leaving behind the two deck ship with a huge\n ballon above and rotor blades strapped to its side.\n Or at least thats how Galileo described it to you.\n"
	intro4 = "After a while, you feel Aster stoping.\n You do the same one step further.\n"
	intro5 = "\nGalileo Asteros:\n  Ah... Feel the gentle breeze, " + player.myPlayer.name + ".\n That was quite a superb jurney, wasn't it? Now here we\n are, at my homeland, the famous floating island of Eldcarseld.\n Well, I think we should get going, plenty of things to\n investigate. Oh, and do not fright, I'm well acquainted with thy\n sight condition, so I will take the liberty to escort thee\n and detail thy surroundings in the best way possible. If thou\n nedst any more information about our current position, just\n ask me to LOOK around and I shall give thee some more details.\n"

	for character in intro1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	for character in intro2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	for character in intro3:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	for character in intro4:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	channel1.play(GALILEO_A)
	for character in intro5:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)

	game_interactivity.print_location()
	main_game_loop()

def game_over_screen():
	os.system('cls')
	channel0.play(death_music)
	notice1 = " It looks like thy eyre has come to an end.\n Well, well, it does not need to stay that way, does it?\n After all, tis but a mere game.\n So, would you like to try again?\n"
	for character in notice1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.07)
	answer = input("> ")
	acceptable_inputs = ['yes', 'no', 'y', 'n']
	
	while answer not in acceptable_inputs:
		confused = " Oh... that's not quite a proper answer, is it?\n"
		for character in confused:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.05)
		answer = input("> ")

	if answer.lower() in ['yes', 'y']:
		notice2 = " Magnificent, let us try this again, shall we?\n"
		for character in notice2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.05)
		time.sleep(2)
		title.title_screen()

	elif answer.lower() in ['no', 'n']:
		notice2 = " Oh... I see.\n Well, that is your decision, right?\n May it be as you wish.\n"
		for character in notice2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.05)
		notice3 = " Farewell,\n fellow glotrotter..."
		for character in notice3:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.1)
		time.sleep(2)
		sys.exit()