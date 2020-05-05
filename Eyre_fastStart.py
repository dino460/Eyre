##########################################################
# DO NOT DISTRIBUTE ; DO NOT REPRODUCE ; DO NOT SELL   ###
# COPYRIGHT 2020 RAPHAEL ZOEGA CALI GOMES              ###
# ALL RIGHT RESERVED                                   ###
##########################################################
# Coded in Python 3.8.0 ####
###############################################
# NOT needed for the game to function.       ##
# Fast start that jumps main menu and intro. ##
###############################################

import cmd
import textwrap
import sys
import os
import time
import random
import winsound
import player
import game_functionality
import game_interactivity
import title
import maps
import combat
import inventory_file

screen_width = 100

game_functionality.setup_game()