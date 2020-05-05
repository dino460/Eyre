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
import game_functionality
import game_interactivity
import title
import maps
import combat
import inventory_file
import player

ZIREL_POTION = False
GORNAN_POTION = False
GORNAN_TALK = False
GORNAN_SIDEQUEST = False
THEOLD_SIDEQUEST = False

# SETTING UP MUSIC WITH PYGAME MIXER
pygame.init() # Initialize Pygame

musicPlayerIcon = pygame.image.load('musicPlayerIcon.png') # Set up pygame window as MUSIC PLAYER
pygame.display.set_mode((250, 50))
pygame.display.set_caption('MUSIC PLAYER')
pygame.display.set_icon(musicPlayerIcon)

GORNAN_A = pygame.mixer.Sound('SFX/GORNAN_A.wav')
GORNAN_B = pygame.mixer.Sound('SFX/GORNAN_B.wav')
GORNAN_C = pygame.mixer.Sound('SFX/GORNAN_C.wav')
GORNAN_D = pygame.mixer.Sound('SFX/GORNAN_D.wav')

LUTHIEN_A = pygame.mixer.Sound('SFX/LUTHIEN_A.wav')
LUTHIEN_B = pygame.mixer.Sound('SFX/LUTHIEN_B.wav')
LUTHIEN_C = pygame.mixer.Sound('SFX/LUTHIEN_C.wav')

DAUGHTER_A = pygame.mixer.Sound('SFX/DAUGHTER_A.wav')
DAUGHTER_B = pygame.mixer.Sound('SFX/DAUGHTER_B.wav')
DAUGHTER_C = pygame.mixer.Sound('SFX/DAUGHTER_C.wav')

POTIONGUY_A = pygame.mixer.Sound('SFX/POTIONGUY_A.wav')
POTIONGUY_B = pygame.mixer.Sound('SFX/POTIONGUY_B.wav')

RUDEZA_A = pygame.mixer.Sound('SFX/RUDEZA_A.wav')
RUDEZA_B = pygame.mixer.Sound('SFX/RUDEZA_B.wav')
RUDEZA_C = pygame.mixer.Sound('SFX/RUDEZA_C.wav')

channel0 = pygame.mixer.Channel(0)
channel0.set_volume(0.3)
channel1 = pygame.mixer.Channel(1)
channel1.set_volume(0.4)

#### LOCATION CHECKER ####
def check_location(location):
	if location == 'city of pandora':
		pandora_npc()
	elif location == 'kor-ok forest north' and GORNAN_TALK == True and GORNAN_SIDEQUEST == False:
		kForestN_npc()
	elif location == 'zirel range':
		zirel_npc()
	else:
		maps.zonemap[player.myPlayer.location][maps.VISITED] = True

#### NPCS INTERACTIONS ####

# NPCS IN PANDORA #
def pandora_npc():
	global GORNAN_POTION
	global GORNAN_SIDEQUEST
	if maps.zonemap[player.myPlayer.location][maps.VISITED] == False:
		notice1 = "\n Galileo Asteros:\n  Albeit Pandora is pratically empty, there still are some\n dwellers, waiting for an uncertain future, hoping for the\n end of this dark times. If it is thy wish, we can\n approach one this inhabitants.\n"
		notice2 = "\n(1) There is a fair skin lady, to our left side. She is adorned\n in a long, clean, bright yellow dress, with delicate white\n gloves on her hands. She is happily watering some flowers\n perfectly arrenged in front of a store called 'Luthien's Flowers'\n"
		notice3 = "\n(2) Some distance from where we stand, a big muscular man dressed\n on simple clothes: a white cotton shirt covered by a smith's\n apron and brown cloth trousers. He nervously walks in\n circles in front of a sealed-off dwelling, swinging left\n and right because of his wooden left leg.\n"
		notice4 = "\n(3) The last one is an old man, covered in a black cloak, standing\n next to the bridge that leads to the northern Kor-ok Forest.\n He appears to be eons old, even though most of his derma is\n veiled by the mantle. He seems to be staring at us,\n thought the reson for this I do not know.\n"
		notice5 = "\n What would thee like to do?\n"

		for character in notice1:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		for character in notice2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		for character in notice3:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		for character in notice4:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		for character in notice5:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)

		print("{You can talk or ignore [quit]}\n")

	elif maps.zonemap[player.myPlayer.location][maps.VISITED] == True:
		notice1 = "\n(1) There is a fair skin lady, to our left side. She is adorned\n in a long, clean, bright yellow dress, with delicate white\n gloves on her hands. She is happily watering some flowers\n perfectly arrenged in front of a store called 'Luthien's Flowers'\n"
		notice2_1 = "\n(2) Some distance from where we stand, a big muscular man dressed\n on simple clothes: a white cotton shirt covered by a smith's\n apron and brown cloth trousers. He nervously walks in\n circles in front of a sealed-off dwelling, swinging left\n and right because of his wooden left leg.\n"
		notice2_2 = "\n(2) Some distance from where we stand, Gornan sits on a wooden\n chair wathcing his daughter as she plays with some dolls in front\n of the same sealed-off dwelling.\n"
		notice3 = "\n(3) The last one is an old man, covered in a black cloak, standing\n next to the bridge that leads to the northern Kor-ok Forest.\n He appears to be eons old, even though most of his derma is\n veiled by the mantle. He seems to be staring at us,\n thought the reson for this I do not know.\n"
		notice4 = "\n What would thee like to do?\n"

		for character in notice1:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.01)
"""
		for character in notice2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.01)
"""
		if GORNAN_SIDEQUEST == False:
			for character in notice2_1:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.01)
		elif GORNAN_SIDEQUEST == True:
			for character in notice2_2:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.01)
		for character in notice4:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.01)

		print("{You can talk or ignore [quit]}\n")

	answer = input("> ")
	maps.zonemap[player.myPlayer.location][maps.VISITED] = True
	acceptable_inputs = ['talk', 'quit']
	while answer.lower() not in acceptable_inputs:
		print("Unknown action.")
		answer = input("> ")

	if answer.lower() == 'talk':
		notice6 = "\n Who would thee like to talk?\n"
		for character in notice6:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)

		answer = input("> ")
		acceptable_inputs = ['1', '2', '3', 'quit']
		while answer.lower() not in acceptable_inputs:
			print("Thou can't talk too this person.\n")
			answer = input("> ")

		if answer == '1':
			os.system('cls')
			channel1.play(LUTHIEN_A)
			interaction1 = "\n Oh, good morning, brave adventurer! You are an aventurer\n right? Your vestiments give it away. How may I help you?\n"
			for character in interaction1:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.03)
			Luthien_interaction()

		elif answer == '2' and GORNAN_SIDEQUEST == False:
			os.system('cls')
			channel1.play(GORNAN_A)
			interaction1 = "\n Hey, you two ther', you ar' adventurers,\n 'ight? Would you pleas' help my?\n"
			for character in interaction1:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.03)
			Gornan_interaction1()

		elif answer == '2' and GORNAN_SIDEQUEST == True:
			os.system('cls')
			channel1.play(GORNAN_C)
			interaction1 = "\n Thank you, adventurers, thank you. There anything I can do for ya?\n"
			for character in interaction1:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.03)
			Gornan_interaction2()

		elif answer == '3' and THEOLD_SIDEQUEST == False:
			os.system('cls')
			interaction1 = "\n Ye art " + player.myPlayer.name + " and G. Aster, am I correct?\n I may have some interesting items for ye but first,\n for this path to be traversed, three\n questions must be answered with accurst.\n"
			for character in interaction1:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.07)
			TheOld_interaction()

		elif answer == '3' and THEOLD_SIDEQUEST == True:
			os.system('cls')
			interaction1 = "\n Ye have no more business with me.\n"
			for character in interaction1:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.07)

		elif answer.lower() == 'quit':
			os.system('cls')
			game_interactivity.print_location()
			game_functionality.main_game_loop()

	elif answer.lower() == 'quit':
		os.system('cls')
		game_interactivity.print_location()
		game_functionality.main_game_loop()


def Luthien_interaction():
	print("(1) What is happening here?")
	print("(2) Who are you?")
	print("(3) Where am I?")
	print("(4) Quit")
	answer = input("> ")

	if answer == '1':
		interaction2 = "\n Do you mean, the Curse? Well, nobody really knows for shure,\n but I bet there is something to do with Gardisen Tower,\n it was sealed-off as soon as the first... things... showed up.\n"
		channel1.play(LUTHIEN_A)
		for character in interaction2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		Luthien_interaction()

	elif answer == '2':
		interaction2 = "\n Oh, my name is Luthien, I live here since\n birth and run this flower shop for quite some time.\n"
		channel1.play(LUTHIEN_B)
		for character in interaction2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		Luthien_interaction()

	elif answer == '3':
		interaction2 = "\n Well, you are in the City of Pandora,\n capital of Eldcarseld, the floating island.\n"
		channel1.play(LUTHIEN_C)
		for character in interaction2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		Luthien_interaction()

	elif answer == '4':
		os.system('cls')
		pandora_npc()

	else:
		os.system('cls')
		print("Unknown action.")
		pandora_npc()


def Gornan_interaction1():
	global GORNAN_POTION
	global GORNAN_SIDEQUEST
	global GORNAN_TALK
	print("(1) What's going on?")
	print("(2) Who are you?")
	print("(3) How can we help you?")
	print("(4) Quit")
	answer = input("> ")

	if answer == '1':
		interaction2 = "\n Me daugh'er has gone to Kor-ok For'st, west of 'ere.\n But it's been an hour an' she hasn't returned since,\n an' I can't go me-self.\n"
		channel1.play(GORNAN_A)
		for character in interaction2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		GORNAN_TALK = True
		Gornan_interaction1()

	elif answer == '2':
		interaction2 = "\n Me name is Gornan, I am the bla'smith 'ere.\n"
		channel1.play(GORNAN_B)
		for character in interaction2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		Gornan_interaction1()

	elif answer == '3' and GORNAN_POTION == False:
		interaction2 = "\n Pleas', you nee'to fin'er, she was look'n for some flowers\n for miss Luth'en in the Kor-ok For'st.\n Pleas' take tis potion to help you.\n"
		channel1.play(GORNAN_D)
		for character in interaction2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		inventory_file.inventory.items.append(inventory_file.potion)
		inventory_file.inventory.current_storage += 1
		GORNAN_POTION = True
		GORNAN_TALK = True
		Gornan_interaction1()

	elif answer == '3' and GORNAN_POTION == True:
		interaction2 = "\n Pleas', you nee'to fin'er, she was look'n for some flowers\n for miss Luth'en in the Kor-ok For'st.\n"
		channel1.play(GORNAN_D)
		for character in interaction2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		GORNAN_TALK = True
		Gornan_interaction1()

	elif answer == '4':
		os.system('cls')
		pandora_npc()

	else:
		os.system('cls')
		print("Unknown action.")
		pandora_npc()

def Gornan_interaction2():
	print("(1) Do you know anything abou The Curse?")
	print("(2) How is the girl doing?")
	print("(3) Any other thing we can help you with?")
	print("(4) Quit")
	answer = input("> ")

	if answer == '1':
		interaction2 = "\n Nay sire. Only that which is tol'in the stories.\n Sorry me can't help ya.\n"
		channel1.play(GORNAN_A)
		for character in interaction2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		Gornan_interaction2()

	elif answer == '2':
		interaction2 = "\n She doin' fine, just taking care she never goes out alon'again.\n"
		channel1.play(GORNAN_C)
		for character in interaction2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		Gornan_interaction2()

	elif answer == '3':
		interaction2 = "\n Not in the moment, no. But if ye nee'some 'elp with anything,\n and I mean, anything, ye just call me-self and I go 'ight away.\n"
		channel1.play(GORNAN_B)
		for character in interaction2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		Gornan_interaction2()

	elif answer == '4':
		os.system('cls')
		pandora_npc()

	else:
		os.system('cls')
		print("Unknown action.")
		pandora_npc()



def TheOld_interaction():
	print("(1) What? Who are you anyway?")
	print("(2) What is this item you are talking about?")
	print("(3) What are the questions?")
	print("(4) Quit")
	answer = input("> ")

	if answer == '1':
		interaction2 = "\n My name have been forgotten in the past,\n along with many other important things.\n"
		for character in interaction2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.07)
		TheOld_interaction()

	elif answer == '2':
		interaction2 = "\n Hoho, if I tell thee it loses all the fun.\n"
		for character in interaction2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.07)
		TheOld_interaction()

	elif answer == '3':
		interaction2 = "\n The first riddle is as follows:\n I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?.\n"
		for character in interaction2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.07)
		print("{The answers have only one word. Use 'quit' to give up at any moment}")
		answer = input("> ")

		while answer.lower() not in ['echo', 'quit']:
			interaction3 = "\n Incorrect!\n"
			for character in interaction3:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.07)
			answer = input("> ")

		if answer.lower() == 'echo':
			interaction3 = "\n Thou art correct! This thing all things devours:\n Birds, beasts, trees, flowers; Gnaws iron, bites steel;\n Grinds hard stones to meal; Slays king, ruins town,\n And beats high mountain down.\n"
			for character in interaction3:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.07)

			answer = input("> ")
			while answer.lower() != 'time':
				interaction4 = "\n Incorrect!\n"
				for character in interaction4:
					sys.stdout.write(character)
					sys.stdout.flush()
					time.sleep(0.07)
				answer = input("> ")

			if answer.lower() == 'time':
				interaction4 = "\n Correct! Now, the last riddle:\n No-legs lay on one-leg,\n two-legs sat near on three-legs,\n four-legs got some.\n"
				for character in interaction4:
					sys.stdout.write(character)
					sys.stdout.flush()
					time.sleep(0.07)
				answer = input("> ")

				while answer.lower() != 'fish on a table, man on a stool, cat gets the scraps':
					interaction5 = "\n Incorrect!\n"
					for character in interaction5:
						sys.stdout.write(character)
						sys.stdout.flush()
						time.sleep(0.07)
					answer = input("> ")

				if answer.lower() == 'fish on a table, man on a stool, cat gets the scraps':
					interaction5 = "\n Who art thee? Oh, I know, you looked it up on the internet, right?\n That is clever, wrong, but clever. Thou may have the item.\n"
					for character in interaction5:
						sys.stdout.write(character)
						sys.stdout.flush()
						time.sleep(0.07)
					inventory_file.inventory.items.append(inventory_file.runic_mark)
					inventory_file.inventory.current_storage += 1

					wait = input("> ")
					global THEOLD_SIDEQUEST
					THEOLD_SIDEQUEST = True
					os.system('cls')
					pandora_npc()

				elif answer.lower() == 'quit':
					os.system('cls')
					pandora_npc()

			elif answer.lower() == 'quit':
				os.system('cls')
				pandora_npc()

		elif answer.lower() == 'quit':
			os.system('cls')
			pandora_npc()

	if answer == '4':
		os.system('cls')
		pandora_npc()

	else:
		os.system('cls')
		print("Unknown action.")
		pandora_npc()


# NPCS IN NORTHERN KOR_OK FOREST #
def kForestN_npc():
	maps.zonemap[player.myPlayer.location][maps.VISITED] = True
	global GORNAN_SIDEQUEST
	notice1 = "\n As soon as you enter in the Northern area of Kor-ok Forest\n you can hear a gentle giggle echoing through the woods.\n"
	notice2 = "\n Galileo Asteros:\n  I bet this is Gornan's little daughter, shall we try to find her?\n"

	for character in notice1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.03)
	for character in notice2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.03)

	answer = input("> ")
	acceptable_inputs = ['y', 'n', 'yes', 'no']
	while answer.lower() not in acceptable_inputs:
		warning = "\n I'm sorry my friend,\n but I could not understand what thee said.\n"
		for character in warning:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		answer = input("> ")

	if answer.lower() in ['y', 'yes']:
		notice3 = "\n As you walk deeper into the forest, the giggling gets louder.\n Sudenly, you feel the sun touching you skin,\n and a open space appears to spread before you.\n"
		notice4 = "\n Galileo Asteros:\n  It's a glade, and... Oh, a little girl is playing with\n the flowers in it's centre. Why, hello there, little one.\n"
		notice5 = "\n What would you like to do?\n"

		for character in notice3:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		for character in notice4:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		for character in notice5:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)

		print("{You can talk to her or ignore [quit]}")
		answer = input("> ")
		acceptable_inputs = ['talk', 'quit']
		while answer.lower() not in acceptable_inputs:
			warning = "\n " + player. myPlayer.name + " what is thee doing, my friend?\n Is everything all right?\n"
			for character in warning:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.03)
				print("{You can talk to her or ignore [quit]}")
			answer = input("> ")

		if answer.lower() == 'talk':
			interaction1 = "\n Girl:\n  Haha, oh, hi mister, how are you?\n Woul'you like to play wi'me? Where's my daddy? Who are you?\n"
			channel1.play(DAUGHTER_A)
			for character in interaction1:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.03)

			print("(1) Calm down girl, where are here to take you to your daddy.")
			print("(2) Hello, I'm fine, thank you. So, your dad is worried you did't return yet...")
			print("(3) Play with you? All right, what are you playing?")

			answer = input("> ")
			acceptable_inputs = ['1', '2', '3']
			while answer.lower() not in acceptable_inputs:
				warning = "\n Wha're you sayin' mister?\n"
				for character in warning:
					sys.stdout.write(character)
					sys.stdout.flush()
					time.sleep(0.03)
				answer = input("> ")

			GORNAN_SIDEQUEST = True

			if answer.lower() == '1':
				interaction2 = "\n Girl:\n  Take me to 'im? Oh, I remenbered, I should have returned\n to 'im, oh no! So'y, I have to go mister!\n"
				interaction3 = "\n Galileo Asteros:\n  Wait a sec... Ah, nevermind, she's already gone.\n Well, I believe we ought to check if she arrived in\n one piece, but it is thy call.\n"
				
				channel1.play(DAUGHTER_B)
				for character in interaction2:
					sys.stdout.write(character)
					sys.stdout.flush()
					time.sleep(0.03)
				for character in interaction3:
					sys.stdout.write(character)
					sys.stdout.flush()
					time.sleep(0.03)

				wait = input("> ")
				os.system('cls')
				game_interactivity.print_location()
				game_functionality.main_game_loop()

			elif answer.lower() == '2':
				interaction2 = "\n Girl:\n  Oh, is he? I need to go apologize to 'im,\n then and say I was playing with the flowers.\n"
				interaction3 = "\n Galileo Asteros:\n  Well, take care, little one, the path is dangerous and...\n"
				interaction4 = "\n Girl:\n  Don't worry mister, I live 'ere since I was little.\n Wait, I'm still little... Hihi.\n"
				interaction5 = "\n Galileo Asteros:\n  " + player.myPlayer.name + ", I believe we ought to check\n if she arrived in one piece, but it is thy call.\n"
				
				channel1.play(DAUGHTER_B)
				for character in interaction2:
					sys.stdout.write(character)
					sys.stdout.flush()
					time.sleep(0.03)
				for character in interaction3:
					sys.stdout.write(character)
					sys.stdout.flush()
					time.sleep(0.03)
				channel1.play(DAUGHTER_C)
				for character in interaction4:
					sys.stdout.write(character)
					sys.stdout.flush()
					time.sleep(0.03)
				for character in interaction5:
					sys.stdout.write(character)
					sys.stdout.flush()
					time.sleep(0.03)

				wait = input("> ")
				os.system('cls')
				game_interactivity.print_location()
				game_functionality.main_game_loop()

			elif answer.lower() == '3':
				interaction2 = "\n Girl:\n  Ohh YOU WILL PLAY WITH ME, YAAAY! I am playing...\n"
				interaction3 = "\n And so you spent some time with Gornan's daughter, until...\n"
				interaction4 = "\n Galileo Asteros:\n  " + player.myPlayer.name + ", I'm afraid we already played\n enough, 'didn't we? This little girl needs to go back to\n her father, he is deeply worried of her absence.\n"
				interaction5 = "\n Girl:\n  He is worried? So, I need to go back.\n Thanks for playing with me mister, it was fun!\n"
				interaction6 = "\n Galileo Asteros:\n  Why, I believe we ought to check if she arrived in one piece, but it is thy call.\n"
				
				channel1.play(DAUGHTER_A)
				for character in interaction2:
					sys.stdout.write(character)
					sys.stdout.flush()
					time.sleep(0.03)
				for character in interaction3:
					sys.stdout.write(character)
					sys.stdout.flush()
					time.sleep(0.03)
				for character in interaction4:
					sys.stdout.write(character)
					sys.stdout.flush()
					time.sleep(0.03)
				channel1.play(DAUGHTER_B)
				for character in interaction5:
					sys.stdout.write(character)
					sys.stdout.flush()
					time.sleep(0.03)
				for character in interaction6:
					sys.stdout.write(character)
					sys.stdout.flush()
					time.sleep(0.03)

				wait = input("> ")
				os.system('cls')
				game_interactivity.print_location()
				game_functionality.main_game_loop()

		elif answer.lower() == 'quit':
			os.system('cls')
			interaction2 = "\n Galileo Asteros:\n  Oh, I see, thou art in haste. Well, at least let us go back\n and warn this girl's father.\n"
			interaction3 = "\n Girl:\n  Wait, you already leving? But we didn't even play...\n"
			interaction4 = "\n Galileo Asteros:\n  Little girl, thou should return to thy father. Farewell.\n"

			for character in interaction2:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.03)
				channel1.play(DAUGHTER_B)
			for character in interaction3:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.03)
			for character in interaction4:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.03)

			wait = input("> ")
			os.system('cls')
			game_interactivity.print_location()
			game_functionality.main_game_loop()

	elif answer.lower() in ['n', 'no']:
		notice = "\nGalileo Asteros:\n  I feel this is not a shrewd decision, but that's on thee.\n"
		for character in notice:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)

		wait = input("> ")
		os.system('cls')
		game_interactivity.print_location()
		game_functionality.main_game_loop()


# NPCS IN ZIREL RANGE #
def zirel_npc():
	global ZIREL_POTION
	if maps.zonemap[player.myPlayer.location][maps.VISITED] == False:
		notice1 = "\n Galileo Asteros:\n Albeit many live here at Zirel Range, for a long time it's\n been hard to make contact with the mountain dwellers.\n But we are quite lucky to find two Eldcarseldians here.\n"
		notice2 = "\n(1) There is a dark skin lady, to our right side. She is adorned\n in a short brown skirt, with a worn grey shirt\n over her torso. She is calmly sharpening an adorned shortsword\n in front of a small cavern entrance, skillfully carved like a house's doorway.\n"
		notice3 = "\n(2) To our left, a small man tries to pin a carabiner inte the\n mountain side. His skin is tanned and his simple clothes\n are worn and sully. He appears to be occupied.\n"
		notice4 = "\n What would thee like to do?\n"

		for character in notice1:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		for character in notice2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		for character in notice3:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		for character in notice4:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)

		print("{You can talk or ignore [quit]}\n")

	elif maps.zonemap[player.myPlayer.location][maps.VISITED] == True:
		notice1 = "\n(1) There is a dark skin lady, to our right side. She is adorned\n in a short brown skirt, with a worn grey shirt\n over her torso. She is calmly sharpening an adorned shortsword\n in front of a small cavern entrance, skillfully carved like a house's doorway.\n"
		notice2 = "\n(2) To our left, a small man tries to pin a carabiner inte the\n mountain side. His skin is tanned and his simple clothes\n are worn and sully. He appears to be occupied.\n"
		notice3 = "\n What would thee like to do?\n"

		for character in notice1:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.01)
		for character in notice2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.01)
		for character in notice3:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.01)

		print("{You can talk or ignore [quit]}\n")

	answer = input("> ")
	maps.zonemap[player.myPlayer.location][maps.VISITED] = True
	acceptable_inputs = ['talk', 'quit']
	while answer.lower() not in acceptable_inputs:
		print("Unknown action.")
		answer = input("> ")

	if answer.lower() == 'talk':
		notice6 = "\n Who would thee like to talk?\n"
		for character in notice6:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)

		answer = input("> ")
		acceptable_inputs = ['1', '2', 'quit']
		while answer not in acceptable_inputs:
			print("Thou can't talk too this person.\n")
			answer = input("> ")

		if answer.lower() == '1':
			os.system('cls')
			interaction1 = "\n Sav'aaq, how may I help you foreigner?\n"
			channel1.play(RUDEZA_A)
			for character in interaction1:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.03)

			Rudeza_interaction()
			
		elif answer.lower() == '2' and ZIREL_POTION == False:
			os.system('cls')
			channel1.play(POTIONGUY_A)
			interaction1 = "\n If you are going to climb a steep mountain, better be prepared.\n Here, take this potion it may be usefull in you jurney.\n"
			for character in interaction1:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.03)
			inventory_file.inventory.items.append(inventory_file.potion)
			inventory_file.inventory.current_storage += 1
			ZIREL_POTION = True

			wait = input("> ")
			os.system('cls')
			zirel_npc()

		elif answer.lower() == '2' and ZIREL_POTION == True:
			os.system('cls')
			channel1.play(POTIONGUY_B)
			interaction1 = "\n If you are going to climb a steep mountain, better be prepared.\n"
			for character in interaction1:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.03)

			wait = input("> ")
			os.system('cls')
			zirel_npc()

		elif answer.lower() == 'quit':
			os.system('cls')
			game_interactivity.print_location()
			game_functionality.main_game_loop()

	elif answer.lower() == 'quit':
		os.system('cls')
		game_interactivity.print_location()
		game_functionality.main_game_loop()

def Rudeza_interaction():
	print("(1) Do you know anything about The Curse?")
	print("(2) Who are you?")
	print("(3) What is 'Sav'aaq'?")
	print("(4) Quit")
	answer = input("> ")

	if answer == '1':
		interaction2 = "\n So you are the one they brought to investigate the curse,\n huh. Well, unfortunately for you I know as much as one of\n these rocks, maybe you should talk do King Camlost,\n he ought to know something.\n"
		channel1.play(RUDEZA_A)
		for character in interaction2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		Rudeza_interaction()

	elif answer == '2':
		interaction2 = "\n I am Rudeza Atawi, from the mountain folk.\n I am a watcher among our ranks.\n"
		channel1.play(RUDEZA_B)
		for character in interaction2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		Rudeza_interaction()

	elif answer == '3':
		interaction2 = "\n It is a compliment here on the mountains, it means 'good day'.\n"
		channel1.play(RUDEZA_C)
		for character in interaction2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.03)
		Rudeza_interaction()

	elif answer == '4':
		os.system('cls')
		zirel_npc()

	else:
		os.system('cls')
		print("Unknown action.")
		zirel_npc()