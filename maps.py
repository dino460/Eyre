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
import combat

#### WORLD MAP ####
"""
_________________________
|		|		|		|
|		|		|		|
|	a1	|	a2	|	a3	|
|_______|_______|_______|
|		|		|		|
|		|		|		|
|	b1	|	b2	|	b3	|
|		|		|		|
|_______|_______|_______|
|		|		|		|
|	c1	|	c2	|	c3	|
|		|		|		|
|_______|_______|_______|
a1: undying falls
a2: nott pass
a3: gardisen tower

b1: kor-ok forest north
b2: city of pandora
b3: quiet hills

c1: kor-ok forest south
c2: zirel range
c3: broken cliff

"""
#### MAP SETUP ####
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
VISITED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {}

zonemap = {
		'undying falls': {
			DESCRIPTION: "The Undying Falls are a cluster of waterfalls and rapids\n that cascade to Taru's Lake, a reservoir amongst towering plateaus.\n The reservoir provides water to the city and Kor-ok forest, southward.\n The exuberant view one can witness when entering this venue\n is only possible due to the constant flow of the rivers throughout\n Eldcarseld, which feed not only the lake,\n but its grottos and its enourmous cave system.\n Once a secure arcadia for swimmers and tourists,\n the Curse brought strange creatures that lurk underwater,\n attacking all who try to swim on Taru's Lake,\n and few who venture the caves ever return.",
			EXAMINATION : "Shapeless shadows swim across the lake. Some grottos are easily\n accessible from where we stand, though I would rather avoid\n getting any closer to those damned places.\n No person is to be seen around here.",
			VISITED: False,
			UP: '',
			DOWN: 'kor-ok forest north',
			LEFT: '',
			RIGHT: 'nott pass',
		},
		'nott pass': {
			DESCRIPTION: "Be carefull with thy steps, for Nott Pass is a\n treacherous trail. Built by dwarfs when they were still\n around, tis passage through Undying Falls' surrounding plateaus\n is remarkably narrow, and the falling rocks only support\n those who claim tis as the most dagnerous place in all\n Eldcarseld. Not much but rocks addornates tis place.",
			EXAMINATION : "Stone over stone.",
			VISITED: False,
			UP: '',
			DOWN: '',
			LEFT: 'undying falls',
			RIGHT: 'gardisen tower',
		},
		'gardisen tower': {
			DESCRIPTION: "Once one cross Nott Pass, if it survives, it is possible\n to lay eyes upon a dazzling blend between man and nature's\n creation. A stone pillar erupts from amidst the plateau.\n There, an immense tower was build impregnated in the obelisk,\n combining man and dwarf's genious into a piece of\n architectonic art. Some elder stories convey of an old\n wizard known as Gardisen who once lived in it and brought\n magic to Eldcarseld. The tower's doors are shut since long\n ago, no one really knows the real motif.",
			EXAMINATION : "Apart from its exquisite architecture, the Gardisen Tower\n and its whereabouts are quite sterile, with a few small bushes\n ocasionaly sprouting in the shadows between some rocks.\n Like the rest of Eldcarseld, the Curse settled in this barren\n land. Here, gusts of wind take unseeable shapes and strike\n inattentive globetrotters, slashing through flesh and bone,\n or throwing them down to the valleys beneath.",
			VISITED: False,
			UP: '',
			DOWN: '',
			LEFT: 'nott pass',
			RIGHT: '',
		},


		'kor-ok forest north': {
			DESCRIPTION: "The treacherous Kor-ok Forest. Many globetrotters have come here\n in the pursuit of great treasures; few have been seen again, and those who have,\n never again dared to explore the forest further than the trails allow.\n This claustrophobie inducing ambient of abounding hefty flora and vast fauna\n is at any time overflowing with life. At least in times past, before the curse.\n It's trees, which used achieve enourmous hights and endure for centuries,\n now wither in despair; its glades, once crowded of animal life, now remain silent, lifeless.\n Kor-ok Forest is now but a memoir of its former glory.",
			EXAMINATION : "An uttermost silence prevail over this once abundant woodland,\n only disturbed by an eventual sound of twigs being broken\n by an obscure creature. Sometimes strange shadows roam between\n the trees evading my sight. But the most idiosyncratic thing\n about it is the impossibility to discern whose\n this shadows belong to.",
			VISITED: False,
			UP: 'undying falls',
			DOWN: 'kor-ok forest south',
			LEFT: '',
			RIGHT: 'city of pandora',
		},
		'city of pandora': {
			DESCRIPTION: "Oh, the City of Pandora, Eldcarseld's crown's jewel. It's great white walls\n stretching through a dozen kilometres, it's many markets thiving with life.\n But, since the Curse plunged this land, seldom will thee find Eldcarseldians\n wandering through Pandora's great arteries, or fervorously bargaining in its\n markets. Pandora is now quasi empty (save for few who believe the worst\n is already past); its buildings, almost all closed and barricated;\n the dirt has started to accru throughout its alleys.\n Tis are merely the bare bones of a once thriving capital.",
			EXAMINATION : "Not much is left to be seen. Few people remain,\n none of Pandora's many markets remain open.\n To better oversee its domains, King Camlost tethered folk's access\n to certain areas of the city, thus, for the time being,\n let us stick to Pandora's main avenue, 'Luthien's Path', which connects\n Quiet Hills, on the EAST, to the northern Kor-ok Forest, to the WEST.",
			VISITED: False,
			UP: '',
			DOWN: '',
			LEFT: 'kor-ok forest north',
			RIGHT: 'quiet hills',
		},
		'quiet hills': {
			DESCRIPTION: "Tis vast field of immaculate hills is used as landing grounds for airships\n and other analogous machines. Almost completely empty, save for\n trifling turf, the Quiet Hills are devoid of animal life,\n and scarse of human presence. Northward of here are the hights\n of Gardisen Tower, innaccessible but from Nott Pass.\n In the south, it is possible to see the Broken Cliff,\n only reachable from Zirel Range's tortuous trails.",
			EXAMINATION : "Even though I would rather praise Quiet Hills exquisite view,\n I must humbly assume, there may not be much for thee to gaze upon here.\n Thou can access Pandora's city main avenue through here by heading west.",
			VISITED: False,
			UP: '',
			DOWN: '',
			LEFT: 'city of pandora',
			RIGHT: '',
		},


		'kor-ok forest south': {
			DESCRIPTION: "This area is quite similar to its twin in the north,\n but in a reduced scale. The trees are considerably less densely packed,\n the glades are more abundant. Being less thriving in animal life,\n it would be normal to believe that southern Kor-ok Forest was a quiet corner,\n nonetheless, it still is a forest, and it used to own quite an honorable\n symphony. Indeed, it used to, but now it remains silent as a crypt.",
			EXAMINATION : "Opposing to its former nature, the southern Kor-ok Forest\n became a dangerous place. In times past, passionate couples would rest\n among the shadows of its sparsely scattered flora.\n At this time any who dares to lay among its shadows may encounter a not intended end,\n for vile creatures roam amongst the low turf and the shifting\n penumbra, waiting for distracted folk.",
			VISITED: False,
			UP: 'kor-ok forest north',
			DOWN: '',
			LEFT: '',
			RIGHT: 'zirel range',
		},
		'zirel range': {
			DESCRIPTION: "Named after the graceful Zirel of Riva this elegantly wind\n sculpted range is often regarded as Eldcarseld's most\n beautiful locale. Spanning all the region south of Pandora\n tis lofty set of mountains is home to many endemic and\n unique species, fauna and flora alike. From the high peaks\n here found one can gaze all of the island territory.\n Through it's many tortuous trails and abundant hiking spots,\n Zirel Range is the exclusive path through which one\n can reach the Broken Cliff",
			EXAMINATION : "At first glance one can be decieved on assuming tis but a\n bare wasteland of rock and small shrubs, nonetheless, some\n Eldcarseldians have found a place to adress as home amidst\n the hights and inside small caves. And said caves, span\n from small grottos to incomprehensibly large cave systems,\n suffused with stuning crystal-like formations and\n creatures with who thou wish not to encounter.",
			VISITED: False,
			UP: '',
			DOWN: '',
			LEFT: 'kor-ok forest south',
			RIGHT: 'broken cliff',
		},
		'broken cliff': {
			DESCRIPTION: "Little is known about what caused the Broken Cliff to be...\n well, broken. Some elder tales allude to a gargantuan\n mystical creature that lacerated a chuck of the isle;\n others say that the Curse emerged from the missing region\n and rotted away, falling back to the lands bellow.\n The region itself is a continuation of Zirel Range that the\n conjectured cataclism caused to be torn appart irregularly.\n Broad stone bridges naturally sculpted by water and wind\n arch through bottomless pits and ragged cliffs.",
			EXAMINATION : "Smugglers and sky pirates used to benefit from the difficulty\n to traverse and access Broken Cliff's many cave systems\n and valleys to hide and contraband goods into Eldcarseld.\n Since the Curse took its hold in the island fewer\n and fewer people risk attempting to traverse tis complex\n labyrinth. For some obscure motif, even the strange shadows and\n the outlandish creatures, spawn of the Curse, are known not to\n come here. Yet, here we are.",
			VISITED: False,
			UP: '',
			DOWN: '',
			LEFT: 'zirel range',
			RIGHT: '',
		},
}