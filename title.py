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
import maps
import combat
import inventory_file

# SETTING UP MUSIC WITH PYGAME MIXER
pygame.init() # Initialize Pygame

musicPlayerIcon = pygame.image.load('musicPlayerIcon.png') # Set up pygame window as MUSIC PLAYER
pygame.display.set_mode((250, 50))
pygame.display.set_caption('MUSIC PLAYER')
pygame.display.set_icon(musicPlayerIcon)

title_music = pygame.mixer.Sound('Music/Title.wav')
intro_music = pygame.mixer.Sound('Music/Intro.wav')
channel0 = pygame.mixer.Channel(0)
channel0.set_volume(0.3)
channel1 = pygame.mixer.Channel(1)

#### Title Screen ####
def title_screen_selections():
	option = input("\n	   > ")

	if option.lower() == ("play"):
		intro()

	elif option.lower() == ("help"):
		help_menu()

	elif option.lower() == ("quit"):
		sys.exit()

	while option.lower() not in ['play', 'help', 'quit']:
		print("Please enter a valid command.")

		option = input("\n	   > ")
		if option.lower() == ("play"):
			intro()
		elif option.lower() == ("help"):
			help_menu()
		elif option.lower() == ("quit"):
			sys.exit()

def title_screen():
	os.system('cls')
	channel0.play(title_music)
	rolling_title()
	title_screen_selections()

def help_menu():
	print('\n' + '- Type your commands to do them -')
	print('- Type "move", then up, down, left or right to move -')
	print('- Use "look" to inspect something -')
	print('- Type "help" once the game has started to open the tutorial file -')
	print('- Good luck and have fun -' + '\n')
	title_screen_selections()

def intro():
	os.system('cls')
	channel0.play(intro_music)
	image = open('eldcarseld.txt', 'r')
	expendable = image.read()
	for character in expendable:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.007)
	image.close()

	print('\n\n\n')

	notice1 = "\nEldcarseld, the land above the clouds, home to the City of Pandora.\n"
	notice2 = "\nMany know only of the tales told about this place, tales from\n adventurers from around the world, tales of a city on top of a floating\n mountain. Few have had the oportunity to bestow eyes upon such place,\n but none who did was ever heard to regret it.\n"
	notice3 = "\nBut some mystifying curse has spread through this exquisite\n land; something never before seen. Odd creatures roam in the dark, shadows\n roam without bodies and bodies roam without shadows.\n"
	notice4 = "\nSome convey of a delirious monarch's acts; a  forgotten king\n from decades past who meddled with forces unknown, but whose\n acts linger to this day.\n"
	notice5 = "\nOthers talk about a new king's deeds, about dark magic and\n cryptic consortiums.\n"
	notice6 = "\nThat's when thou enter, a foreign globetrotter from a land\n far in the realms in Eastfold. An explorer and investigator\n that, spite thy sight conditions, have made thyself\n a name amongst the others.\n"
	notice7 = "\nI, Galileo Asteros, also notorious simply as Aster, have\n summoned thee to solve this enigma, and so may we part from\n Eastfold to Eldcarseld.\n"
	notice8 = "\nBut first...\n"

	for character in notice1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.06)
	for character in notice2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.06)
	for character in notice3:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.07)
	for character in notice4:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.07)
	for character in notice5:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.082)
	for character in notice6:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.06)
	for character in notice7:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.06)
	for character in notice8:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.1)

	input("> ")
	game_functionality.setup_game()

def rolling_title():

	print('	   > Quit <')
	time.sleep(0.1)
	os.system('cls')

	print('	   > Help <')
	print('	   > Quit <')
	time.sleep(0.1)
	os.system('cls')

	print('	   > Play <')
	print('	   > Help <')
	print('	   > Quit <')
	time.sleep(0.1)
	os.system('cls')

	print('#' * 34)
	print('	   > Play <')
	print('	   > Help <')
	print('	   > Quit <')
	time.sleep(0.1)
	os.system('cls')

	print('\n' + '#' * 34)
	print('	   > Play <')
	print('	   > Help <')
	print('	   > Quit <')
	time.sleep(0.1)
	os.system('cls')

	print(' #######    #    #     # #######')
	print('\n' + '#' * 34)
	print('	   > Play <')
	print('	   > Help <')
	print('	   > Quit <')
	time.sleep(0.1)
	os.system('cls')

	print(' #          #    #    #  #      ')
	print(' #######    #    #     # #######')
	print('\n' + '#' * 34)
	print('	   > Play <')
	print('	   > Help <')
	print('	   > Quit <')
	time.sleep(0.1)
	os.system('cls')

	print(' #          #    #   #   #      ')
	print(' #          #    #    #  #      ')
	print(' #######    #    #     # #######')
	print('\n' + '#' * 34)
	print('	   > Play <')
	print('	   > Help <')
	print('	   > Quit <')
	time.sleep(0.1)
	os.system('cls')

	print(' #####      #    ######  #####  ')
	print(' #          #    #   #   #      ')
	print(' #          #    #    #  #      ')
	print(' #######    #    #     # #######')
	print('\n' + '#' * 34)
	print('	   > Play <')
	print('	   > Help <')
	print('	   > Quit <')
	time.sleep(0.1)
	os.system('cls')

	print(' #         # #   #     # #      ')
	print(' #####      #    ######  #####  ')
	print(' #          #    #   #   #      ')
	print(' #          #    #    #  #      ')
	print(' #######    #    #     # #######')
	print('\n' + '#' * 34)
	print('	   > Play <')
	print('	   > Help <')
	print('	   > Quit <')
	time.sleep(0.1)
	os.system('cls')

	print(' #        #   #  #     # #      ')
	print(' #         # #   #     # #      ')
	print(' #####      #    ######  #####  ')
	print(' #          #    #   #   #      ')
	print(' #          #    #    #  #      ')
	print(' #######    #    #     # #######')
	print('\n' + '#' * 34)
	print('	   > Play <')
	print('	   > Help <')
	print('	   > Quit <')
	time.sleep(0.1)
	os.system('cls')

	print(' ####### #     # ######  #######')
	print(' #        #   #  #     # #      ')
	print(' #         # #   #     # #      ')
	print(' #####      #    ######  #####  ')
	print(' #          #    #   #   #      ')
	print(' #          #    #    #  #      ')
	print(' #######    #    #     # #######')
	print('\n' + '#' * 34)
	print('	   > Play <')
	print('	   > Help <')
	print('	   > Quit <')
	time.sleep(0.1)
	os.system('cls')

	print('')
	print(' ####### #     # ######  #######')
	print(' #        #   #  #     # #      ')
	print(' #         # #   #     # #      ')
	print(' #####      #    ######  #####  ')
	print(' #          #    #   #   #      ')
	print(' #          #    #    #  #      ')
	print(' #######    #    #     # #######')
	print('\n' + '#' * 34)
	print('	   > Play <')
	print('	   > Help <')
	print('	   > Quit <')
	time.sleep(0.1)
	os.system('cls')

	print('#' * 34 + '\n')
	print(' ####### #     # ######  #######')
	print(' #        #   #  #     # #      ')
	print(' #         # #   #     # #      ')
	print(' #####      #    ######  #####  ')
	print(' #          #    #   #   #      ')
	print(' #          #    #    #  #      ')
	print(' #######    #    #     # #######')
	print('\n' + '#' * 34)
	print('	   > Play <')
	print('	   > Help <')
	print('	   > Quit <')
	time.sleep(0.1)
	os.system('cls')


	print('\n' + '#' * 34 + '\n')
	print(' ####### #     # ######  #######')
	print(' #        #   #  #     # #      ')
	print(' #         # #   #     # #      ')
	print(' #####      #    ######  #####  ')
	print(' #          #    #   #   #      ')
	print(' #          #    #    #  #      ')
	print(' #######    #    #     # #######')
	print('\n' + '#' * 34)
	print('	   > Play <')
	print('	   > Help <')
	print('	   > Quit <')