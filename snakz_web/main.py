import asyncio
import pygame
import random
from collections import deque
pygame.init() # initialise pygame #

grey = (80,80,80)		# définit les couleurs #
red = (235,100,100)
green = (120,235,120)

display_width = 800		# définit la largeur de la fenêtre #
display_height = 640	# définit la hauteur de la fenêtre #
area_width = 760		# la largeur de la zone de jeu #
area_height = 560		# la hauteur de la zone de jeu #
border_size = 20		# écart entre la bordure de la fenêtre et celle de la zone de jeu #

gameDisplay = pygame.display.set_mode((display_width,display_height))	# définit les dimensions de la fenêtre #
pygame.display.set_caption('SnakZ')										# affiche le titre du jeu #
icon = pygame.image.load('snakeZicon2.png')			# importe l'icône du jeu #
pygame.display.set_icon(icon)						# affiche l'icône #

img_one = pygame.image.load('snakeone.png')			# importe l'image de la tête du serpent 1 #
img_two = pygame.image.load('snaketwo.png')			# importe l'image de la tête du serpent 2 #
snakeHidden_img = pygame.image.load('snakeHidden.png')		# importe l'image de la tête qui sera utilisée lors de la mort d'un serpent #
appleimg = pygame.image.load('appleZ.png')			# importe l'image de la pomme #

lifeSlot_img = pygame.image.load('lifeSlot.png')
lifeOne_img = pygame.image.load('lifeOne.png')		# importe l'image d'un coeur rouge #
lifeTwo_img = pygame.image.load('lifeTwo.png')		# importe l'image d'un coeur vert #
lifeEmpty_img = pygame.image.load('lifeEmpty.png')		# importe l'image d'un coeur vide #

boostSpeed_img = pygame.image.load('boostSpeed.png')	# importe l'image du boost de vitesse #
boostSpeed_circle_img = pygame.image.load('boostSpeed_circle.png')	# l'image du boost de vitesse sans le cercle #
timeLimit_speed = 120		# durée du boost de vitesse #

boostDouble_img = pygame.image.load('boostDouble.png')
boostDouble_circle_img = pygame.image.load('boostDouble_circle.png')
timeLimit_double = 90

boostShield_img = pygame.image.load('boostShield.png')
boostShield_circle_img = pygame.image.load('boostShield_circle.png')
timeLimit_shield = 60

boostLaser_img = pygame.image.load('boostLaser.png')
boostLaser_circle_img = pygame.image.load('boostLaser_circle.png')
laserfirst_img = pygame.image.load('laserfirst.png')	# premier bout de laser #
laser_img = pygame.image.load('laser.png')		# le reste #
timeLimit_laser = 90

boostCircle1_one = pygame.image.load('boostCircle1_red.png')	# pour l'animation de durée des boosts #
boostCircle2_one = pygame.image.load('boostCircle2_red.png')
boostCircle3_one = pygame.image.load('boostCircle3_red.png')
boostCircle4_one = pygame.image.load('boostCircle4_red.png')
boostCircle5_one = pygame.image.load('boostCircle5_red.png')
boostCircle6_one = pygame.image.load('boostCircle6_red.png')
boostCircle7_one = pygame.image.load('boostCircle7_red.png')
boostCircle8_one = pygame.image.load('boostCircle8_red.png')
boostCircles_one = [boostCircle1_one, boostCircle2_one, boostCircle3_one, boostCircle4_one, boostCircle5_one, boostCircle6_one, boostCircle7_one, boostCircle8_one]

boostCircle1_two = pygame.image.load('boostCircle1_green.png')
boostCircle2_two = pygame.image.load('boostCircle2_green.png')
boostCircle3_two = pygame.image.load('boostCircle3_green.png')
boostCircle4_two = pygame.image.load('boostCircle4_green.png')
boostCircle5_two = pygame.image.load('boostCircle5_green.png')
boostCircle6_two = pygame.image.load('boostCircle6_green.png')
boostCircle7_two = pygame.image.load('boostCircle7_green.png')
boostCircle8_two = pygame.image.load('boostCircle8_green.png')
boostCircles_two = [boostCircle1_two, boostCircle2_two, boostCircle3_two, boostCircle4_two, boostCircle5_two, boostCircle6_two, boostCircle7_two, boostCircle8_two]

aleaBoost = 505		# rareté des boosts #
sprintstock_limit = 140		# l'endurance max #

clock = pygame.time.Clock()				# définit le temps #

lifeNb_one = 3		# 3 vies pour le serpent 1 au lancement du jeu #
lifeNb_two = 3		# 3 vies pour le serpent 2 au lancement du jeu #

block_size = 20			# définit la largeur et la hauteur d'un bloc #
gameSpeed = 15				# définit la vitesse du jeu #
game_mode = 1				# 1 = un joueur contre le bot, 2 = deux joueurs #
bot_mistake_chance = 0.25	# probabilité que le bot ne réfléchisse pas pendant une boucle (le rend battable) #

background_img = pygame.image.load('SNAKZbackground.png')	# image de fond #
bgline_img = pygame.image.load('bgline.png')		# ligne grise pour le fond #

menuselect_img = pygame.image.load('menuselect.png')	# sélection dans le menu #
menu1player_img = pygame.image.load('menu(1player).png')	# 1 joueur sélectionné #
menu2players_img = pygame.image.load('menu(2players).png')

paused_img = pygame.image.load('paused.png')	# écran pause #
pausedplay_img = pygame.image.load('paused(play).png')
pausedmenu_img = pygame.image.load('paused(menu).png')

bgshad_img = pygame.image.load('bgshad.png')	# contour du jeu sombre #
screen_img = pygame.image.load('SNAKZscreen.png')	# effet écran #
p1wins_img = pygame.image.load('p1wins.png')	# joueur 1 gagne #
p2wins_img = pygame.image.load('p2wins.png')
draw_img = pygame.image.load('draw.png')

title_img = pygame.image.load('title.png')		# les différentes images du titre #
title1_img = pygame.image.load('title1.png')
title2_img = pygame.image.load('title2.png')
title3_img = pygame.image.load('title3.png')
title4_img = pygame.image.load('title4.png')
title5_img = pygame.image.load('title5.png')
titles = [title1_img, title2_img, title3_img, title4_img, title5_img]
for w in range(15):
	titles.append(title_img)


# ------- on créer d'abord des fonctions qu'on utilisera plus tard ------------------------------------------------------------------------------------------------------------------------------ #

async def game_intro():		# page d'accueil #
	global game_mode
	print("Menu: Space to play or pause")
	print("Controls: Arrow Keys / WASD / ZQSD")		# on écrit les contrôles sur l'idle python #
	print("Boosts: rShift / lShift (both work in 1 player mode)")
	print("Restart: R")
	print("Change gameSpeed: + / - / Enter(num)")
	print("Boost Generator: 1 / 2 / 3 / 4 (num)")
	print("If you run into your opponent, you die !")
	intro = True
	while intro:	# tant que intro = True #
		for event in pygame.event.get():
			if event.type == pygame.QUIT:				# si on appuie sur le bouton Quitter de la fenêtre #
				pygame.quit()
				quit()									# ferme la fenêtre #
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:		# flèches = on change de mode #
					game_mode = 3 - game_mode
				if event.key == pygame.K_SPACE:			# si on appuie sur Espace #
					intro = False						# on sort de la boucle intro, le jeu commence #
				if event.key == pygame.K_ESCAPE:		# si on appuie sur Echap #
					pygame.quit()
					quit()								# ferme la fenêtre #
		gameDisplay.blit(background_img, (0,0))		# on affiche le background #
		global randBg_anim
		randBg_anim = True
		randBg()					# affiche des bandes grises sur le background #
		t = random.randrange(20)
		gameDisplay.blit(titles[t], (0,0))			# à chaque boucle, on affiche un des titres stockés dans titles #
		gameDisplay.blit(menuselect_img, (0, 0))	# affiche 1 player, 2 players, options #
		if game_mode == 1:
			gameDisplay.blit(menu1player_img, (0, 0))	# la sélection est sur 1 joueur #
		else:
			gameDisplay.blit(menu2players_img, (0, 0))	# la sélection est sur 2 joueurs #
		gameDisplay.blit(bgshad_img, (0, 0))		# affiche l'ombre #
		gameDisplay.blit(screen_img, (0, 0))		# affiche le faux écran #

		pygame.display.update()				# réactualise l'affichage #
		clock.tick(gameSpeed)
		await asyncio.sleep(0)					# la boucle intro proc speed = 15 fois par seconde #

randBg_change = True
def randBg():
	global randBg_change
	global randBg_list

	if randBg_anim == True:
		c = random.randrange(6)
		if c == 0:
			randBg_change = True

	if randBg_change == True:
		randBg_list = []
		for l in range(3):
			randBgY = random.randrange(border_size, border_size + area_height)
			randBgT = pygame.transform.scale(bgline_img, (display_width, random.randrange(2,10)))
			randBg_list.insert(l*2, randBgT)
			randBg_list.insert((l*2)+1, randBgY)
		randBg_change = False

	for l in range(3):
		gameDisplay.blit(randBg_list[l*2], (0, randBg_list[(l*2)+1]))

async def pause():																# fonction pause #
	global gameSpeed
	global zis1
	global zis2
	global zis3
	global zis4
	global lifeNb_one
	global lifeNb_two
	paused = True															# paused = vrai #
	pause_choice = "play"				# PLAY ou MENU, choisi avec les flèches #
	game_frame = gameDisplay.copy()		# on garde l'image du jeu pour pouvoir redessiner le menu par-dessus #

	def draw_pause():
		gameDisplay.blit(game_frame, (0, 0))
		gameDisplay.blit(paused_img, (0, 0))
		if pause_choice == "play":
			gameDisplay.blit(pausedplay_img, (0, 0))
		else:
			gameDisplay.blit(pausedmenu_img, (0, 0))
		pygame.display.update()												# réactualise l'affichage #

	draw_pause()

	while paused:										# tant que paused = vrai #
		for event in pygame.event.get():									
			if event.type == pygame.QUIT:				# si on appuie sur le bouton Quitter de la fenêtre #
				pygame.quit()
				quit()									# ferme la fenêtre #
			if event.type == pygame.KEYDOWN:						
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:	# flèches = on change de choix #
					if pause_choice == "play":
						pause_choice = "menu"
					else:
						pause_choice = "play"
					draw_pause()
				if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:		# Espace ou Entrée valide le choix #
					if pause_choice == "play":
						paused = False						# paused = faux -> on sort de la boucle paused, le jeu reprend #
					else:
						lifeNb_one = 3					# retour au menu : la prochaine partie repart avec 3 vies #
						lifeNb_two = 3
						await game_intro()
						await gameLoop()
				elif event.key == pygame.K_ESCAPE:		# si on appuie sur Echap #
					pygame.quit()
					quit()								# ferme la fenêtre #

				if event.key == pygame.K_r:
					lifeNb_one = 3
					lifeNb_two = 3
					await gameLoop()	

				if event.key == pygame.K_KP_PLUS:
					gameSpeed += 2
				if event.key == pygame.K_KP_MINUS:
					gameSpeed -= 2
				if event.key == pygame.K_KP_ENTER:
					print("gameSpeed =", gameSpeed)

				if event.key == pygame.K_KP1:
					zis1 = True
				if event.key == pygame.K_KP2:
					zis2 = True
				if event.key == pygame.K_KP3:
					zis3 = True
				if event.key == pygame.K_KP4:
					zis4 = True					

		clock.tick(gameSpeed)
		await asyncio.sleep(0)								# tant que paused = vrai, la fonction proc speed = 15 fois par seconde #

def randSpawn():		# renvoie des coordonnées aléatoires dans la zone de jeu #
	randSpawnX = round(random.randrange(border_size, border_size + area_width - block_size) / block_size) * block_size
	randSpawnY = round(random.randrange(border_size, border_size + area_height - block_size) / block_size) * block_size
	return randSpawnX, randSpawnY

def slots(s):		# définit l'emplacement slots de vies et de boosts #
	slotX = border_size + s*block_size
	slotY = border_size + area_height + block_size
	return slotX, slotY

slot1_one = slots(20)		# définit l'emplacement des slots de boosts #
slot2_one = slots(22)
slot3_one = slots(24)
slot4_one = slots(26)
slot1_two = slots(17)
slot2_two = slots(15)
slot3_two = slots(13)
slot4_two = slots(11)

slotLife1_one = slots(36)	# les slots pour les coeurs #
slotLife2_one = slots(34)
slotLife3_one = slots(32)
slotLife1_two = slots(1)
slotLife2_two = slots(3)
slotLife3_two = slots(5)

def snake_one(block_size, snakeList_one, snake_one_hide):	# affiche la tête du serpent 1 #
	snake_one_list = [img_one, snakeHidden_img]		# la liste contient la tête normale et la tête noire #
	if snake_one_hide == True:
		del snake_one_list[0]	# on supprime img_one donc snakeHidden_img se retrouve à l'emplacement [0] #

	if direction_one == "right":								# si sa direction = droite #
		head_one = pygame.transform.rotate(snake_one_list[0], 270)		# tourne l'image de la tête de 270° #
	elif direction_one == "left":
		head_one = pygame.transform.rotate(snake_one_list[0], 90)
	elif direction_one == "up":
		head_one = snake_one_list[0]
	elif direction_one == "down":
		head_one = pygame.transform.rotate(snake_one_list[0], 180)	
	gameDisplay.blit(head_one, (snakeList_one[-1][0], snakeList_one[-1][1]))	# affiche l'image de la tête après rotation #

def snake_two(block_size, snakeList_two, snake_two_hide):		# idem pour serpent 2 #
	snake_two_list = [img_two, snakeHidden_img]
	if snake_two_hide == True:
		del snake_two_list[0]

	if direction_two == "right":
		head_two = pygame.transform.rotate(snake_two_list[0], 270)
	if direction_two == "left":
		head_two = pygame.transform.rotate(snake_two_list[0], 90)
	if direction_two == "up":
		head_two = snake_two_list[0]
	if direction_two == "down":
		head_two = pygame.transform.rotate(snake_two_list[0], 180)	
	gameDisplay.blit(head_two, (snakeList_two[-1][0], snakeList_two[-1][1]))

def lifeOne(snake_one_hide):		# affiche 1, 2 ou 3 coeurs en fonction du nombre de vie du serpent 1 #
	if snake_one_hide == False:
		if lifeNb_one >= 1:	
			gameDisplay.blit(lifeOne_img, (slotLife1_one))
		if lifeNb_one >= 2:
			gameDisplay.blit(lifeOne_img, (slotLife2_one))
		if lifeNb_one >= 3:
			gameDisplay.blit(lifeOne_img, (slotLife3_one))
	else:						# prépare l'animation de mort #
		if lifeNb_one == 1:
			gameDisplay.blit(lifeEmpty_img, (slotLife1_one))
		if lifeNb_one == 2:
			gameDisplay.blit(lifeEmpty_img, (slotLife2_one))
		if lifeNb_one == 3:
			gameDisplay.blit(lifeEmpty_img, (slotLife3_one))

def lifeTwo(snake_two_hide):
	if snake_two_hide == False:
		if lifeNb_two >= 1:
			gameDisplay.blit(lifeTwo_img, (slotLife1_two))
		if lifeNb_two >= 2:
			gameDisplay.blit(lifeTwo_img, (slotLife2_two))
		if lifeNb_two >= 3:
			gameDisplay.blit(lifeTwo_img, (slotLife3_two))
	else:
		if lifeNb_two == 1:
			gameDisplay.blit(lifeEmpty_img, (slotLife1_two))
		if lifeNb_two == 2:
			gameDisplay.blit(lifeEmpty_img, (slotLife2_two))
		if lifeNb_two == 3:
			gameDisplay.blit(lifeEmpty_img, (slotLife3_two))

def boostSpeed_display_one(time_boostspeed_one, slot_speed):	# affiche l'image correspondante au temps restant du boost #
	c = 0
	for b in boostCircles_one:
		gameDisplay.blit(boostCircles_one[c], (slot_speed))
		if time_boostspeed_one > (c+1)*timeLimit_speed/8:
			c += 1 
	gameDisplay.blit(boostSpeed_circle_img, (slot_speed))
def boostDouble_display_one(time_boostdouble_one, slot_double):
	c = 0
	for b in boostCircles_one:
		gameDisplay.blit(boostCircles_one[c], (slot_double))
		if time_boostdouble_one > (c+1)*timeLimit_double/8:
			c += 1 
	gameDisplay.blit(boostDouble_circle_img, (slot_double))
def boostShield_display_one(time_boostshield_one, slot_shield):
	c = 0
	for b in boostCircles_one:
		gameDisplay.blit(boostCircles_one[c], (slot_shield))
		if time_boostshield_one > (c+1)*timeLimit_shield/8:
			c += 1 
	gameDisplay.blit(boostShield_circle_img, (slot_shield))
def boostLaser_display_one(time_boostlaser_one, slot_laser):
	c = 0
	for b in boostCircles_one:
		gameDisplay.blit(boostCircles_one[c], (slot_laser))
		if time_boostlaser_one > (c+1)*timeLimit_laser/8:
			c += 1 
	gameDisplay.blit(boostLaser_circle_img, (slot_laser))	

def boostSpeed_display_two(time_boostspeed_two, slot_speed):
	c = 0
	for b in boostCircles_two:
		gameDisplay.blit(boostCircles_two[c], (slot_speed))
		if time_boostspeed_two > (c+1)*timeLimit_speed/8:
			c += 1 
	gameDisplay.blit(boostSpeed_circle_img, (slot_speed))
def boostDouble_display_two(time_boostdouble_two, slot_double):
	c = 0
	for b in boostCircles_two:
		gameDisplay.blit(boostCircles_two[c], (slot_double))
		if time_boostdouble_two > (c+1)*timeLimit_double/8:
			c += 1 
	gameDisplay.blit(boostDouble_circle_img, (slot_double))
def boostShield_display_two(time_boostshield_two, slot_shield):
	c = 0
	for b in boostCircles_two:
		gameDisplay.blit(boostCircles_two[c], (slot_shield))
		if time_boostshield_two > (c+1)*timeLimit_shield/8:
			c += 1 
	gameDisplay.blit(boostShield_circle_img, (slot_shield))
def boostLaser_display_two(time_boostlaser_two, slot_laser):
	c = 0
	for b in boostCircles_two:
		gameDisplay.blit(boostCircles_two[c], (slot_laser))
		if time_boostlaser_two > (c+1)*timeLimit_laser/8:
			c += 1 
	gameDisplay.blit(boostLaser_circle_img, (slot_laser))	

def boostDisplay_one(boostType_one, boost_speed_one, boost_double_one, boost_shield_one, boost_laser_one, slot1_one, slot2_one, slot3_one, slot4_one):	# affiche les boosts dans l'ordre d'obtention #
	boostSlots_one = [slot1_one, slot2_one, slot3_one, slot4_one]
	boostPos_one = 0
	for j in boostType_one:
		if j == "speed":
			boostSpeed_display_one(time_boostspeed_one, boostSlots_one[boostPos_one])
		elif j == "double":
			boostDouble_display_one(time_boostdouble_one, boostSlots_one[boostPos_one])
		elif j == "shield":
			boostShield_display_one(time_boostshield_one, boostSlots_one[boostPos_one])
		elif j == "laser":
			boostLaser_display_one(time_boostlaser_one, boostSlots_one[boostPos_one])
		boostPos_one += 1

def boostDisplay_two(boostType_two, boost_speed_two, boost_double_two, boost_shield_two, boost_laser_two, slot1_two, slot2_two, slot3_two, slot4_two):
	boostSlots_two = [slot1_two, slot2_two, slot3_two, slot4_two]
	boostPos_two = 0
	for j in boostType_two:
		if j == "speed":
			boostSpeed_display_two(time_boostspeed_two, boostSlots_two[boostPos_two])
		elif j == "double":
			boostDouble_display_two(time_boostdouble_two, boostSlots_two[boostPos_two])
		elif j == "shield":
			boostShield_display_two(time_boostshield_two, boostSlots_two[boostPos_two])
		elif j == "laser":
			boostLaser_display_two(time_boostlaser_two, boostSlots_two[boostPos_two])
		boostPos_two += 1

# ------- les 2 fonctions suivantes sont essentielles ------------------------------------------------------------------------------------------------------------------------------ #

# cette fonction affiche tout ce qui constituent le jeu #
def gameDisp(lead_x_one, lead_y_one, lead_x_two, lead_y_two, randAppleX_one,randAppleY_one, randAppleX_two, randAppleY_two, zis1, zis2, zis3, zis4, boostType_one, boostType_two, sprintstock_one, sprintstock_two, boostSpeedX, boostSpeedY, boostDoubleX, boostDoubleY, boostShieldX, boostShieldY, boostLaserX, boostLaserY, boost_speed_one, boost_double_one, boost_shield_one, boost_laser_one, laser_active_one, laser_list_one, slot1_one, slot2_one, slot3_one, slot4_one, boost_speed_two, boost_double_two, boost_shield_two, boost_laser_two, laser_active_two, laser_list_two, slot1_two, slot2_two, slot3_two, slot4_two, snake_one_hide, snake_two_hide, gameOver_win_two):

	gameDisplay.blit(background_img, (0, 0))	# background #
	randBg()		# bandes grises #
	pygame.draw.rect(gameDisplay, grey, (border_size, border_size + area_height - 1, 143, 8), 2)							# limites de la barre de sprint verte #
	pygame.draw.rect(gameDisplay, grey, (display_width - border_size - 143, border_size + area_height - 1, 143, 8), 2)		# limites de la barre de sprint rouge #
	pygame.draw.line(gameDisplay, grey, (display_width/2, 2*border_size + area_height), (display_width/2, 3*border_size + area_height), 2)	# le trait qui sépare les infos des deux serpents #

	gameDisplay.blit(appleimg, (randAppleX_one, randAppleY_one))	# affiche l'image de la pomme 1 avec des coordonnées aléatoires #
	gameDisplay.blit(appleimg, (randAppleX_two, randAppleY_two))	# affiche l'image de la pomme 2 avec des coordonnées aléatoires #

	if zis1 == True:
		gameDisplay.blit(boostSpeed_img, (boostSpeedX, boostSpeedY))	# affiche l'image du boost aléatoirement #
	if zis2 == True:
		gameDisplay.blit(boostDouble_img, (boostDoubleX, boostDoubleY))
	if zis3 == True:
		gameDisplay.blit(boostShield_img, (boostShieldX, boostShieldY))
	if zis4 == True:
		gameDisplay.blit(boostLaser_img, (boostLaserX, boostLaserY))	

	for XnY in snakeList_one[:-1]:														# pour tous les x et y de snakeList_one sauf le dernier élément de la liste #
		pygame.draw.rect(gameDisplay, red, [XnY[0],XnY[1],block_size,block_size])		# dessine un rectangle ( dans la fenêtre, rouge, ( X,  Y, largeur, hauteur ) ) #
	for XnY in snakeList_two[:-1]:
		pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])
	snake_one(block_size, snakeList_one, snake_one_hide)		# affiche la tête du serpent 1 #
	snake_two(block_size, snakeList_two, snake_two_hide)		# la tête du serpent 2 #
	if boost_shield_one == True or gameOver_win_two:		# si le boost de bouclier du serpent 1 est actif ou si serpent 2 gagne #
		snake_one(block_size, snakeList_one, snake_one_hide)	# on réaffiche par dessus la tête du serpent 1 #

	if laser_active_one == True:		# si le laser est activé #
		if (direction_one == "right" and lead_x_one != area_width) or (direction_one == "left" and lead_x_one != border_size) or (direction_one == "up" and lead_y_one != border_size) or (direction_one == "down" and lead_y_one != area_height):
			if direction_one == "right" and lead_x_one != area_width:
				laserfirstR_img = pygame.transform.rotate(laserfirst_img, 270)
				laserR_img = pygame.transform.rotate(laser_img, 90)
			elif direction_one == "left" and lead_x_one != border_size:
				laserfirstR_img = pygame.transform.rotate(laserfirst_img, 90)
				laserR_img = pygame.transform.rotate(laser_img, 90)
			elif direction_one == "up" and lead_y_one != border_size:
				laserfirstR_img = laserfirst_img
				laserR_img = laser_img
			elif direction_one == "down" and lead_y_one != area_height:
				laserfirstR_img = pygame.transform.rotate(laserfirst_img, 180)
				laserR_img = laser_img

			gameDisplay.blit(laserfirstR_img, (laser_list_one[0]))	# affiche l'image, préalablement tournée, aux coordonnées situées à la première place de laser_list_one #
			for eachLaserblock in laser_list_one[1:]:	# chaque élément de laser_list_one contient une liste de 2 élements (X et Y); pour tous les éléments de laser_list_one à partir du 2ème #
				gameDisplay.blit(laserR_img, (eachLaserblock[0], eachLaserblock[1]))

	if laser_active_two == True:
		if (direction_two == "right" and lead_x_two != area_width) or (direction_two == "left" and lead_x_two != border_size) or (direction_two == "up" and lead_y_two != border_size) or (direction_two == "down" and lead_y_two != area_height):
			if direction_two == "right" and lead_x_two != area_width:
				laserfirstR_img = pygame.transform.rotate(laserfirst_img, 270)
				laserR_img = pygame.transform.rotate(laser_img, 90)
			elif direction_two == "left" and lead_x_two != border_size:
				laserfirstR_img = pygame.transform.rotate(laserfirst_img, 90)
				laserR_img = pygame.transform.rotate(laser_img, 90)
			elif direction_two == "up" and lead_y_two != border_size:
				laserfirstR_img = laserfirst_img
				laserR_img = laser_img
			elif direction_two == "down" and lead_y_two != area_height:
				laserfirstR_img = pygame.transform.rotate(laserfirst_img, 180)
				laserR_img = laser_img

			gameDisplay.blit(laserfirstR_img, (laser_list_two[0]))
			for eachLaserblock in laser_list_two[1:]:
				gameDisplay.blit(laserR_img, (eachLaserblock[0], eachLaserblock[1]))

	pygame.draw.rect(gameDisplay, grey, (border_size, border_size, area_width, area_height), 2)		# trace les limites de la zone de jeu #
	for s in [1,3,5,32,34,36]:
		gameDisplay.blit(lifeSlot_img, (slots(s)))		# affiche des coeurs vides #
		gameDisplay.blit(lifeEmpty_img, (slots(s)))
	lifeOne(snake_one_hide)		# affiche des coeurs remplis en fonction du nombre de vie restant #
	lifeTwo(snake_two_hide)

	if len(boostType_one) >= 1:
		boostDisplay_one(boostType_one, boost_speed_one, boost_double_one, boost_shield_one, boost_laser_one, slot1_one, slot2_one, slot3_one, slot4_one)	# affiche les boosts en bas de l'écran #
	if len(boostType_two) >= 1:
		boostDisplay_two(boostType_two, boost_speed_two, boost_double_two, boost_shield_two, boost_laser_two, slot1_two, slot2_two, slot3_two, slot4_two)	# affiche les boosts en bas de l'écran #

	if boost_laser_one == False:
		pygame.draw.rect(gameDisplay, red, (display_width - sprintstock_one - border_size - 1, border_size + area_height + 1, sprintstock_one, 5))	# affiche les barres d'endurances #
	else:
		pygame.draw.rect(gameDisplay, grey, (display_width - sprintstock_one - border_size - 1, border_size + area_height + 1, sprintstock_one, 5))		# si boost_laser_one = Vrai, alors la barre d'endurance est grise #
	if boost_laser_two == False:
		pygame.draw.rect(gameDisplay, green, (border_size + 2, border_size + area_height + 1, sprintstock_two, 5))
	else:
		pygame.draw.rect(gameDisplay, grey, (border_size + 2, border_size + area_height + 1, sprintstock_two, 5))

	gameDisplay.blit(bgshad_img, (0, 0))	# affiche l'ombre #
	gameDisplay.blit(screen_img, (0, 0))	# affiche le faux écran #


# cette fonction est lancée quand quelqu'un meurt #
async def animation_death(gameOver_draw, gameOver_win_two, gameOver_win_one, block_size, snakeList_one, snakeList_two, lead_x_one, lead_y_one, lead_x_two, lead_y_two, randAppleX_one,randAppleY_one, randAppleX_two, randAppleY_two, zis1, zis2, zis3, zis4, boostType_one, boostType_two, sprintstock_one, sprintstock_two, boostSpeedX, boostSpeedY, boostDoubleX, boostDoubleY, boostShieldX, boostShieldY, boostLaserX, boostLaserY, boost_speed_one, boost_double_one, boost_shield_one, boost_laser_one, laser_active_one, laser_list_one, slot1_one, slot2_one, slot3_one, slot4_one, boost_speed_two, boost_double_two, boost_shield_two, boost_laser_two, laser_active_two, laser_list_two, slot1_two, slot2_two, slot3_two, slot4_two, snake_one_hide, snake_two_hide): # fait clignoter la tête du serpent qui perd #
	for n in range(1,8):
		if n == 1 or n == 3 or n == 5 or n == 7:	# la tête devient noire pendant 0.25s #
			if gameOver_draw == True:
				snake_one_hide = True
				snake_two_hide = True
			elif gameOver_win_two == True:
				snake_one_hide = True
				snake_two_hide = False
			elif gameOver_win_one == True:
				snake_two_hide = True	
				snake_one_hide = False
			gameDisp(lead_x_one, lead_y_one, lead_x_two, lead_y_two, randAppleX_one,randAppleY_one, randAppleX_two, randAppleY_two, zis1, zis2, zis3, zis4, boostType_one, boostType_two, sprintstock_one, sprintstock_two, boostSpeedX, boostSpeedY, boostDoubleX, boostDoubleY, boostShieldX, boostShieldY, boostLaserX, boostLaserY, boost_speed_one, boost_double_one, boost_shield_one, boost_laser_one, laser_active_one, laser_list_one, slot1_one, slot2_one, slot3_one, slot4_one, boost_speed_two, boost_double_two, boost_shield_two, boost_laser_two, laser_active_two, laser_list_two, slot1_two, slot2_two, slot3_two, slot4_two, snake_one_hide, snake_two_hide, gameOver_win_two)		
				# on relance la boucle gameDisp, cette fois avec les paramètres qui permettent d'afficher la tête en noir #
			pygame.display.update()		# on actualise l'affichage #
			await asyncio.sleep(0.25)	# le temps s'arrête pendant 0.25 s #
		elif n == 2 or n == 4 or n == 6:		# la tête reprend sa couleur initiale pendant 0.1s #
			if gameOver_draw == True:
				snake_one_hide = False
				snake_two_hide = False
			elif gameOver_win_two == True:
				snake_one_hide = False
			elif gameOver_win_one == True:
				snake_two_hide = False
			gameDisp(lead_x_one, lead_y_one, lead_x_two, lead_y_two, randAppleX_one,randAppleY_one, randAppleX_two, randAppleY_two, zis1, zis2, zis3, zis4, boostType_one, boostType_two, sprintstock_one, sprintstock_two, boostSpeedX, boostSpeedY, boostDoubleX, boostDoubleY, boostShieldX, boostShieldY, boostLaserX, boostLaserY, boost_speed_one, boost_double_one, boost_shield_one, boost_laser_one, laser_active_one, laser_list_one, slot1_one, slot2_one, slot3_one, slot4_one, boost_speed_two, boost_double_two, boost_shield_two, boost_laser_two, laser_active_two, laser_list_two, slot1_two, slot2_two, slot3_two, slot4_two, snake_one_hide, snake_two_hide, gameOver_win_two)		
			pygame.display.update()
			await asyncio.sleep(0.1)



# ------- le bot du mode 1 joueur : il conduit le serpent 2 ------------------------------------------------------------------------------------------------------------------------------------- #

bot_moves = {"left": (-1, 0), "right": (1, 0), "up": (0, -1), "down": (0, 1)}
bot_opposite = {"left": "right", "right": "left", "up": "down", "down": "up"}
bot_cols = area_width // block_size		# nombre de cases en largeur #
bot_rows = area_height // block_size	# nombre de cases en hauteur #

def bot_cell(x, y):		# transforme des coordonnées en pixels en une case de la grille (les bords se rejoignent) #
	return (int((x - border_size) // block_size) % bot_cols, int((y - border_size) // block_size) % bot_rows)

def bot_step(cell, direction):		# la case voisine dans une direction #
	dx, dy = bot_moves[direction]
	return ((cell[0] + dx) % bot_cols, (cell[1] + dy) % bot_rows)

def bot_direction(head_x, head_y, direction, enemy_list, enemy_direction, targets):	# choisit la prochaine direction du bot #
	if random.random() < bot_mistake_chance:
		return direction

	start = bot_cell(head_x, head_y)
	blocked = set(bot_cell(x, y) for x, y in enemy_list)	# le corps de l'adversaire #
	goals = set(bot_cell(x, y) for x, y in targets)		# pommes et boosts #
	cut_off = {}		# case devant l'adversaire -> nombre de boucles avant qu'il y arrive #
	if enemy_list:
		enemy_head = bot_cell(enemy_list[-1][0], enemy_list[-1][1])
		for d in bot_moves:
			blocked.add(bot_step(enemy_head, d))		# les cases où la tête adverse peut aller #
		ahead = enemy_head
		for n in range(1, 6):
			ahead = bot_step(ahead, enemy_direction)
			if n >= 2:
				cut_off[ahead] = n		# le bot essaie de lui couper la route, s'il peut y arriver avant lui #

	first_move = {}		# pour chaque case atteinte, la première direction prise pour y arriver #
	distance = {}		# le nombre de cases pour y arriver #
	queue = deque()
	for d in bot_moves:
		if d == bot_opposite[direction]:	# un serpent ne peut pas faire demi-tour #
			continue
		cell = bot_step(start, d)
		if cell in blocked:
			continue
		first_move[cell] = d
		distance[cell] = 1
		queue.append(cell)

	while queue:		# parcours en largeur : on trouve l'objectif le plus proche #
		cell = queue.popleft()
		if cell in goals or (cell in cut_off and distance[cell] < cut_off[cell]):
			return first_move[cell]
		for d in bot_moves:
			nxt = bot_step(cell, d)
			if nxt not in blocked and nxt not in first_move and nxt != start:
				first_move[nxt] = first_move[cell]
				distance[nxt] = distance[cell] + 1
				queue.append(nxt)

	if first_move:		# aucun objectif atteignable : on part vers la direction qui laisse le plus de place #
		room = {}
		for d in first_move.values():
			room[d] = room.get(d, 0) + 1
		return max(room, key=room.get)
	return direction

def bot_laser_hits(head_x, head_y, direction, target_x, target_y):	# vrai si la cible est dans la ligne de tir (le laser ne traverse pas les bords) #
	dx, dy = bot_moves[direction]
	if dx != 0:
		return target_y == head_y and (target_x - head_x) * dx > 0
	return target_x == head_x and (target_y - head_y) * dy > 0

# ------- c'est la boucle principale ------------------------------------------------------------------------------------------------------------------------------------------------------------ #

async def gameLoop():
	global gameSpeed				# permet de modifier ou d'utiliser des variables qui sont hors de la fonction GameLoop() #
	global direction_one
	global direction_two
	global gameOver_draw
	global gameOver_win_two
	global gameOver_win_one
	global snakeList_one
	global snakeList_two
	global lifeNb_one
	global lifeNb_two
	global snake_one_hide
	global snake_two_hide
	global time_boostspeed_one
	global time_boostdouble_one
	global time_boostshield_one
	global time_boostspeed_two
	global time_boostdouble_two
	global time_boostshield_two
	global time_boostlaser_one
	global time_boostlaser_two
	global slot_speed
	global slot_double
	global slot_shield
	global slot_laser
	global zis1
	global zis2
	global zis3
	global zis4

	direction_one = 'left'				# direction du serpent 1 = gauche au début de la partie #
	direction_two = 'right'				# direction du serpent 2 = droite au début de la partie #
	direction_change_one = False
	direction_change_two = False
	gameExit = False					# empêche la boucle gameExit de se lancer #
	gameOver = False					# empêche la boucle gameOver de se lancer #
	lives_counted = False				# les vies de la manche n'ont pas encore été retirées #
	gameOver_win_one = False			# serpent 1 n'a pas gagné #
	gameOver_win_two = False			# serpent 2 n'a pas gagné #
	gameOver_draw = False

	loopNb = 0		# c'est le numéro de la boucle actuelle #

	lead_x_one = border_size + area_width			# X du serpent 1 juste à droite de la bordure droite, au début de la partie #
	lead_y_one = border_size + (area_height / 2)		# Y du serpent 1 à la moitié de la hauteur de la fenêtre #
	lead_x_two = 0							# X du serpent 2 juste à gauche de la bordure gauche, au début de la partie #
	lead_y_two = border_size + (area_height / 2)		# Y du serpent 2 à la moitié de la hauteur de la fenêtre #

	lead_x_change_one = -20			# fait avancer le X serpent 1 vers la gauche #
	lead_y_change_one = 0			# Y du serpent 1 ne change pas #
	lead_x_change_two = 20			# fait avancer le X serpent 2 vers la droite #
	lead_y_change_two = 0			# Y du serpent 2 ne change pas #

	snakeList_one = []				# c'est la liste dans laquelle on va stocker toutes les coordonnées prises par le serpent 1 #
	snakeLenght_one = 5				# on commence avec 5 cases #
	snakeList_two = []				# c'est la liste dans laquelle on va stocker toutes les coordonnées prises par le serpent 2 #		
	snakeLenght_two = 5				# on commence avec 5 cases #

	randAppleX_one, randAppleY_one = randSpawn()		# on va chercher les coordonnées de la pomme 1 dans la fonction randSpawn() #
	randAppleX_two, randAppleY_two = randSpawn()		# on va chercher les coordonnées de la pomme 2 dans la fonction randSpawn() #

	boostSpeedX, boostSpeedY = randSpawn()			# cherche les coordonnées du boost de vitesse #
	boostDoubleX, boostDoubleY = randSpawn()		# cherche les coordonnées du boost de multiplication #
	boostShieldX, boostShieldY = randSpawn()		# cherche les coordonnées du boost de bouclier #
	boostLaserX, boostLaserY = randSpawn()			# cherche les coordonnées du boost de laser #

	zis1 = False	# le boost de vitesse n'est pas autorisé à spawn #
	zis2 = False	# le boost de multiplication n'est pas autorisé à spawn #
	zis3 = False	# le boost de bouclier n'est pas autorisé à spawn #
	zis4 = False

	snake_one_hide = False		# l'animation de mort n'est pas autorisée à se lancer #
	snake_two_hide = False

	boostType_one = []		# serpent 1 commence avec 0 boost actif, on y stockera le type de chaque boost, dans l'ordre d'obtention #
	boostType_two = []		# serpent 2 commence avec 0 boost actif #

	boost_speed_one = False		# aucun boost n'est actif #
	boost_speed_two = False
	boost_double_one = False
	boost_double_two = False
	boost_shield_one = False
	boost_shield_two = False

	boost_laser_one = False		# le boost de laser est désactivé #
	laser_active_one = False	# le laser n'est pas actif #
	laser_list_one = []			# va plus tard stocker les coordonnées de chaque bloc de laser #
	boost_laser_two = False
	laser_active_two = False
	laser_list_two = []

	sprint_one = False		# le sprint est inactif #
	sprint_two = False
	sprintstock_one = 0		# l'endurance est rénitialisé #
	sprintstock_two = 0

	while not gameExit:					# tant que gameExit n'est pas vrai #

# ------- si quelqu'un meurt -------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

		while gameOver == True:					# tant que gameOver = vrai #
			
			if lives_counted == False:		# on ne retire les vies qu'une fois par manche, pas à chaque boucle de l'écran de fin #
				lives_counted = True
				if gameOver_draw == True and lifeNb_one > 0 and lifeNb_two > 0:		# si il y a égalité #
					lifeNb_two -= 1									# les deux serpents perdent une vie #
					lifeNb_one -= 1
				elif gameOver_win_two == True and lifeNb_one > 0:	# si le serpent 2 gagne #
					lifeNb_one -= 1									# serpent 1 perd 1 vie #
				elif gameOver_win_one == True and lifeNb_two > 0:	# si le serpent 1 gagne #
					lifeNb_two -= 1									# serpent 2 perd une vie #

			if lifeNb_one == 0 or lifeNb_two == 0:
				gameDisplay.blit(background_img, (0, 0))
				randBg()				
				if lifeNb_one == 0 and lifeNb_two == 0:
					gameDisplay.blit(draw_img, (0,0))
				elif lifeNb_two == 0:
					gameDisplay.blit(p1wins_img, (0,0))
				elif lifeNb_one == 0:
					gameDisplay.blit(p2wins_img, (0,0))
				gameDisplay.blit(bgshad_img, (0, 0))
				gameDisplay.blit(screen_img, (0, 0))
				pygame.display.update()		
			else:
				await gameLoop()		# si personne n'a perdu, on relance gameLoop() #																	# réactualise l'affichage #

			for event in pygame.event.get():
				if event.type == pygame.QUIT:			# si on appuie sur le bouton Quitter de la fenêtre #
					pygame.quit()			# la fenêtre se ferme #
					quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:	# si on appuie sur Echap #
						pygame.quit()		
						quit()				# la fenêtre se ferme #
					if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:		# Espace ou Entrée à la fin d'une partie = MENU #
						lifeNb_one = 3					# les deux serpents reprennent 3 vies #
						lifeNb_two = 3
						await game_intro()				# retour au menu #
						await gameLoop()						# puis le jeu se relance #

			clock.tick(gameSpeed)
			await asyncio.sleep(0)		# laisse le navigateur respirer (pygbag) #


# ------- on affecte les touches ---------------------------------------------------------------------------------------------------------------------------------------------------------------- #

		if loopNb > 0:
			direction_change_one = True		# vrai = le serpent 1 a le droit de changer sa direction #
			direction_change_two = True		# vrai = le serpent 2 a le droit de changer sa direction #

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_r:
					lifeNb_one = 3
					lifeNb_two = 3
					await gameLoop()	

				if event.key == pygame.K_KP_PLUS:
					gameSpeed += 2
				if event.key == pygame.K_KP_MINUS:
					gameSpeed -= 2
				if event.key == pygame.K_KP_ENTER:
					print("gameSpeed =", gameSpeed)

				if event.key == pygame.K_LEFT:				# si on appuie sur la flèche Gauche #
					if not direction_one == "right":		# et si la direction du serpent 1 =/= droite #
						if direction_change_one == True:
							direction_one = "left"				# direction du serpent 1 = gauche #
							lead_x_change_one = -block_size		# la tête du serpent 1 se déplace vers la gauche #
							lead_y_change_one = 0				# la tête du serpent 1 ne se déplace ni vers le bas, ni vers le haut #
							direction_change_one = False

				elif event.key == pygame.K_RIGHT:
					if not direction_one == "left":
						if direction_change_one == True:
							direction_one = "right"
							lead_x_change_one = block_size
							lead_y_change_one = 0
							direction_change_one = False

				elif event.key == pygame.K_UP:
					if not direction_one == "down":
						if direction_change_one == True:
							direction_one = "up"
							lead_y_change_one = -block_size
							lead_x_change_one = 0
							direction_change_one = False
						
				elif event.key == pygame.K_DOWN:
					if not direction_one == "up":
						if direction_change_one == True:
							direction_one = "down"
							lead_y_change_one = block_size
							lead_x_change_one = 0
							direction_change_one = False

				if event.key == pygame.K_RSHIFT or (game_mode == 1 and event.key == pygame.K_LSHIFT):		# active le sprint du serpent 1 (les deux Maj en mode 1 joueur), sauf lorsque le boost laser est actif, dans ce cas le bouton active le laser #
					if boost_laser_one == True and laser_active_one == False:
						laser_active_one = True
					elif sprintstock_one > 0:
						sprint_one = True

				elif event.key == pygame.K_SPACE:			# si on appuie sur Espace #
					await pause()									# on lance la boucle pause() #

				if game_mode == 2 and event.key in (pygame.K_a, pygame.K_q):					# idem pour serpent 2 #
					if not direction_two == "right":
						if direction_change_two == True:
							direction_two = "left"
							lead_x_change_two = -block_size
							lead_y_change_two = 0
							direction_change_two = False

				elif game_mode == 2 and event.key == pygame.K_d:
					if not direction_two == "left":
						if direction_change_two == True:
							direction_two = "right"
							lead_x_change_two = block_size
							lead_y_change_two = 0
							direction_change_two = False

				elif game_mode == 2 and event.key in (pygame.K_w, pygame.K_z):
					if not direction_two == "down":
						if direction_change_two == True:
							direction_two = "up"
							lead_y_change_two = -block_size
							lead_x_change_two = 0
							direction_change_two = False

				elif game_mode == 2 and event.key == pygame.K_s:
					if not direction_two == "up":
						if direction_change_two == True:
							direction_two = "down"
							lead_y_change_two = block_size
							lead_x_change_two = 0
							direction_change_two = False

				if game_mode == 2 and event.key == pygame.K_LSHIFT:		# active le sprint du serpent 2 #
					if boost_laser_two == True and laser_active_two == False:
						laser_active_two = True
					elif sprintstock_two > 0:
						sprint_two = True

				if event.key == pygame.K_KP1:
					zis1 = True
				if event.key == pygame.K_KP2:
					zis2 = True
				if event.key == pygame.K_KP3:
					zis3 = True
				if event.key == pygame.K_KP4:
					zis4 = True

			if event.type == pygame.KEYUP:			# tant que la touche est maintenue, le sprint est actif #
				if event.key == pygame.K_RSHIFT or (game_mode == 1 and event.key == pygame.K_LSHIFT):
					sprint_one = False
				if game_mode == 2 and event.key == pygame.K_LSHIFT:
					sprint_two = False


		if game_mode == 1 and direction_change_two == True:		# en mode 1 joueur, le bot conduit le serpent 2 #
			targets = [[randAppleX_one, randAppleY_one], [randAppleX_two, randAppleY_two]]
			if zis1 == True:
				targets.append([boostSpeedX, boostSpeedY])
			if zis2 == True:
				targets.append([boostDoubleX, boostDoubleY])
			if zis3 == True:
				targets.append([boostShieldX, boostShieldY])
			if zis4 == True:
				targets.append([boostLaserX, boostLaserY])
			bot_choice = bot_direction(lead_x_two, lead_y_two, direction_two, snakeList_one, direction_one, targets)
			if bot_choice != direction_two:
				direction_two = bot_choice
				lead_x_change_two = bot_moves[bot_choice][0] * block_size
				lead_y_change_two = bot_moves[bot_choice][1] * block_size
				direction_change_two = False
			if boost_laser_two == True and laser_active_two == False and bot_laser_hits(lead_x_two, lead_y_two, direction_two, lead_x_one, lead_y_one):
				laser_active_two = True		# le bot tire quand le joueur est dans sa ligne de mire #

# ------------ on fait avancer le serpent, vérifie s'il passe sur une pomme ou un boost, et calcule les collisions ----------------------------------------------------------------------------------------------------------------------------- #
		F = 1		# les serpents avancent de 1 case par loop #
		if sprint_one == True or sprint_two == True:	# si le sprint est activé, le serpent avance de 3 cases #
			F = 3

		for f in range(F):
			if gameOver == False:	# on s'assure à chaque tour que personne n'a perdu #

				# on s'occupe du serpent 1 #
				if f == 0 or sprint_one == True:	# si le sprint 1 est actif la boucle s'éxécute 3 fois, sinon 1 fois seulement #

					if laser_active_one == False:	# si le laser est actif le serpent s'arrête pendant un court instant #
						lead_x_one += lead_x_change_one			# X du serpent 1 = X du serpent 1 + X qui change en fonction de sa direction #
						lead_y_one += lead_y_change_one			# Y du serpent 1 = Y du serpent 1 + Y qui change en fonction de sa direction #

					if lead_x_one >= border_size + area_width:					# si le serpent 1 sort de la zone de jeu, il ressort de l'autre côté #
						lead_x_one = border_size
					elif lead_x_one < border_size:
						lead_x_one = border_size + area_width - block_size
					elif lead_y_one >= border_size + area_height:
						lead_y_one = border_size
					elif lead_y_one < border_size:
						lead_y_one = border_size + area_height - block_size		

					if laser_active_one == False:		# seulement si le laser n'est pas déclenché #
						snakeHead_one = []								# crée une liste vide appelée snakeHead_one #
						snakeHead_one.append(lead_x_one)				# y ajoute X de la tête du serpent 1 #
						snakeHead_one.append(lead_y_one)				# y ajoute Y de la tête du serpent 1 #
						snakeList_one.append(snakeHead_one)				# ajoute à snakeList_one les coordonnées de la tête du serpent 1 #

					while len(snakeList_one) > snakeLenght_one:		# tant que la longueur de snakeList_one > longueur autorisée #
						del snakeList_one[0]						# supprime les coordonnées à la 1ère place de la liste, c'est-à-dire le bout de la queue #

					if lead_x_one == randAppleX_one and lead_y_one == randAppleY_one:		# on vérifie si le serpent 1 passe sur une pomme ou un boost #
						randAppleX_one, randAppleY_one = randSpawn()	# s'il passe sur une pomme, les coordonnées de la prochaine pomme sont redemandées #
						snakeLenght_one +=2				# le serpent gagne 2 cases de longueur #
						if boost_double_one == True:
							snakeLenght_one +=2			# si le boost Double est actif, il en regagne 2 #
					if lead_x_one == randAppleX_two and lead_y_one == randAppleY_two:
						randAppleX_two, randAppleY_two = randSpawn()
						snakeLenght_one +=2
						if boost_double_one == True:
							snakeLenght_one +=2		

					if lead_x_one == boostSpeedX and lead_y_one == boostSpeedY:		# s'il passe sur le boost de vitesse #
						time_boostspeed_one = 0			# le timer est réinitialisé #
						if boost_speed_one == False:	# s'il n'est pas déja actif #
							boost_speed_one = True	
							boostType_one.append("speed")			# le nombre de boosts actifs du serpent augmente de 1 #
						boostSpeedX, boostSpeedY = randSpawn()		# on redemande les coordonnées du prochain boost #				
						zis1 = False		# le boost de vitesse n'est plus autorisé à spawn #
					if lead_x_one == boostDoubleX and lead_y_one == boostDoubleY:
						time_boostdouble_one = 0
						if boost_double_one == False:
							boost_double_one = True
							boostType_one.append("double")
						boostDoubleX, boostDoubleY = randSpawn()
						zis2 = False
					if lead_x_one == boostShieldX and lead_y_one == boostShieldY:
						time_boostshield_one = 0
						if boost_shield_one == False:
							boost_shield_one = True	
							boostType_one.append("shield")
						boostShieldX, boostShieldY = randSpawn()
						zis3 = False
					if lead_x_one == boostLaserX and lead_y_one == boostLaserY:
						time_boostlaser_one = 0
						if boost_laser_one == False:
							boost_laser_one = True	
							boostType_one.append("laser")
						boostLaserX, boostLaserY = randSpawn()
						zis4 = False

					if laser_active_one == True:	# lorsque l'on active le laser  #
						laser_list_one = []			# va stocker les coordonnées de chaque bloc du laser #
						laser_block = []		# va stocker temporairement X et Y de chaque bloc #
						if direction_one == "right":		# si la tête est tournée vers la droite #
							laser_block.append(lead_x_one + block_size)		# on ajoute X du premier bloc à la laser_block #
							laser_block.append(lead_y_one)					# on ajoute Y #
							laser_list_one.append(laser_block)			# cette liste contenant X et Y du premier bloc est ajoutée à laser_list_one #
							h = 0
							while laser_block[0] < border_size+area_width-block_size:	# les blocs de laser sont générés jusqu'à atteindre les limites de la zone de jeu #
								laser_block = []
								laser_block.append(lead_x_one + (h+2)*block_size)
								laser_block.append(lead_y_one)
								laser_list_one.append(laser_block)
								h += 1
						if direction_one == "left":
							laser_block.append(lead_x_one - block_size)
							laser_block.append(lead_y_one)
							laser_list_one.append(laser_block)
							h = 0
							while laser_block[0] > border_size:
								laser_block = []
								laser_block.append(lead_x_one - (h+2)*block_size)
								laser_block.append(lead_y_one)
								laser_list_one.append(laser_block)
								h += 1					
						if direction_one == "up":
							laser_block.append(lead_x_one)
							laser_block.append(lead_y_one - block_size)
							laser_list_one.append(laser_block)
							h = 0
							while laser_block[1] > border_size:
								laser_block = []
								laser_block.append(lead_x_one)
								laser_block.append(lead_y_one - (h+2)*block_size)
								laser_list_one.append(laser_block)
								h += 1	
						if direction_one == "down":
							laser_block.append(lead_x_one)
							laser_block.append(lead_y_one + block_size)
							laser_list_one.append(laser_block)
							h = 0
							while laser_block[1] < border_size+area_height-block_size:
								laser_block = []
								laser_block.append(lead_x_one)
								laser_block.append(lead_y_one + (h+2)*block_size)
								laser_list_one.append(laser_block)
								h += 1									


				# puis du serpent 2 #
				if f == 0 or sprint_two == True:	# si le sprint 2 est actif la boucle s'éxécute 3 fois, sinon 1 fois seulement #

					if laser_active_two == False:
						lead_x_two += lead_x_change_two
						lead_y_two += lead_y_change_two		

					if lead_x_two >= border_size + area_width:
						lead_x_two = border_size
					elif lead_x_two < border_size:
						lead_x_two = border_size + area_width - block_size
					elif lead_y_two >= border_size + area_height:
						lead_y_two = border_size
					elif lead_y_two < border_size:
						lead_y_two = border_size + area_height - block_size	

					if laser_active_two == False:
						snakeHead_two = []
						snakeHead_two.append(lead_x_two)
						snakeHead_two.append(lead_y_two)
						snakeList_two.append(snakeHead_two)		

					while len(snakeList_two) > snakeLenght_two:
						del snakeList_two[0]		

					if lead_x_two == randAppleX_one and lead_y_two == randAppleY_one:
						randAppleX_one, randAppleY_one = randSpawn()
						snakeLenght_two +=2
						if boost_double_two == True:
							snakeLenght_two +=2			
					if lead_x_two == randAppleX_two and lead_y_two == randAppleY_two:
						randAppleX_two, randAppleY_two = randSpawn()
						snakeLenght_two +=2
						if boost_double_two == True:
							snakeLenght_two +=2				

					if lead_x_two == boostSpeedX and lead_y_two == boostSpeedY:
						time_boostspeed_two = 0
						if boost_speed_two == False:
							boost_speed_two = True
							boostType_two.append("speed")
						boostSpeedX, boostSpeedY = randSpawn()
						zis1 = False
					if lead_x_two == boostDoubleX and lead_y_two == boostDoubleY:
						time_boostdouble_two = 0
						if boost_double_two == False:
							boost_double_two = True
							boostType_two.append("double")
						boostDoubleX, boostDoubleY = randSpawn()
						zis2 = False
					if lead_x_two == boostShieldX and lead_y_two == boostShieldY:
						time_boostshield_two = 0
						if boost_shield_two == False:
							boost_shield_two = True
							boostType_two.append("shield")
						boostShieldX, boostShieldY = randSpawn()
						zis3 = False
					if lead_x_two == boostLaserX and lead_y_two == boostLaserY:
						time_boostlaser_two = 0
						if boost_laser_two == False:
							boost_laser_two = True	
							boostType_two.append("laser")
						boostLaserX, boostLaserY = randSpawn()
						zis4 = False

					if laser_active_two == True:
						laser_list_two = []
						laser_block = []
						if direction_two == "right":
							laser_block.append(lead_x_two + block_size)
							laser_block.append(lead_y_two)
							laser_list_two.append(laser_block)
							h = 0
							while laser_block[0] < border_size+area_width-block_size:
								laser_block = []
								laser_block.append(lead_x_two + (h+2)*block_size)
								laser_block.append(lead_y_two)
								laser_list_two.append(laser_block)
								h += 1
						if direction_two == "left":
							laser_block.append(lead_x_two - block_size)
							laser_block.append(lead_y_two)
							laser_list_two.append(laser_block)
							h = 0
							while laser_block[0] > border_size:
								laser_block = []
								laser_block.append(lead_x_two - (h+2)*block_size)
								laser_block.append(lead_y_two)
								laser_list_two.append(laser_block)
								h += 1					
						if direction_two == "up":
							laser_block.append(lead_x_two)
							laser_block.append(lead_y_two - block_size)
							laser_list_two.append(laser_block)
							h = 0
							while laser_block[1] > border_size:
								laser_block = []
								laser_block.append(lead_x_two)
								laser_block.append(lead_y_two - (h+2)*block_size)
								laser_list_two.append(laser_block)
								h += 1	
						if direction_two == "down":
							laser_block.append(lead_x_two)
							laser_block.append(lead_y_two + block_size)
							laser_list_two.append(laser_block)
							h = 0
							while laser_block[1] < border_size+area_height-block_size:
								laser_block = []
								laser_block.append(lead_x_two)
								laser_block.append(lead_y_two + (h+2)*block_size)
								laser_list_two.append(laser_block)
								h += 1			


				# si un laser est activé, on calcule s'il touche et où #
				if laser_active_one == True:
					laserHit_pos = 0
					for eachLaserblock in laser_list_one:		# pour chaque élément (contenant X et Y de chaque bloc de laser) de laser_list_one #
						if eachLaserblock == snakeHead_two:		# = coordonnées de la tête de l'autre serpent #
							if boost_shield_two == False:
								gameOver = True
								gameOver_win_one = True			# serpent 1 gagne #
						segmentPos = 0
						for eachSegment in snakeList_two:		# pour chaque bloc laser qui touche un bout de la queue #
							if eachSegment == eachLaserblock:	# on commence par la fin du serpent #
								if segmentPos > laserHit_pos:
									laserHit_pos = segmentPos	# et on garde le bloc touché le plus proche de la tête (si le laser traverse plusieurs fois le serpent) #
							segmentPos += 1
					if boost_shield_two == False:
						snakeLenght_two -= laserHit_pos			# la longueur de l'autre serpent diminue (du bloc touché jusqu'à la fin) #

				if laser_active_two == True:
					laserHit_pos = 0
					for eachLaserblock in laser_list_two:
						if eachLaserblock == snakeHead_one:
							if boost_shield_one == False:
								gameOver = True
								gameOver_win_two = True
						segmentPos = 0						
						for eachSegment in snakeList_one:
							if eachSegment == eachLaserblock:
								if segmentPos > laserHit_pos:
									laserHit_pos = segmentPos
							segmentPos += 1
					if boost_shield_one == False:
						snakeLenght_one -= laserHit_pos					

				# on calcule s'il y a collision à chaque fois : un serpent perd si sa tête touche l'autre serpent, tête comprise #
				# (face à face, de côté ou à travers les bords, la règle est la même pour les deux serpents) #
				if snakeHead_one in snakeList_two and boost_shield_one == False:	# la tête du serpent 1 touche le serpent 2 #
					gameOver = True
					gameOver_win_two = True
				if snakeHead_two in snakeList_one and boost_shield_two == False:	# la tête du serpent 2 touche le serpent 1 #
					gameOver = True
					gameOver_win_one = True
				if gameOver_win_one == True and gameOver_win_two == True:		# les deux perdent en même temps : égalité #
					gameOver_draw = True

# ------- on s'occupe des boosts et du sprint, puis on lance la boucle gameDisp() qui va afficher le jeu ---------------------------------------------------------------------------------------- #

		if boost_speed_one == True:		# si le boost de vitesse est actif #
			sprintstock_one += 7		# l'endurance augmente de 7 en plus par boucle #
			time_boostspeed_one += 1			# on rajoute 1 au timer #
			if time_boostspeed_one > timeLimit_speed:			# si le timer est dépassé #
				boost_speed_one = False		# le boost n'est plus activé #
				boostType_one.remove("speed")			# on enlève dans la liste des boosts actifs, l'élément "speed" #
		if boost_speed_two == True:
			sprintstock_two += 7
			time_boostspeed_two += 1
			if time_boostspeed_two > timeLimit_speed:
				boost_speed_two = False
				boostType_two.remove("speed")

		if boost_double_one == True:
			time_boostdouble_one += 1
			if time_boostdouble_one > timeLimit_double:
				boost_double_one = False
				boostType_one.remove("double")
		if boost_double_two == True:
			time_boostdouble_two += 1
			if time_boostdouble_two > timeLimit_double:
				boost_double_two = False
				boostType_two.remove("double")

		if boost_shield_one == True:
			time_boostshield_one += 1
			if time_boostshield_one > timeLimit_shield:
				boost_shield_one = False
				boostType_one.remove("shield")
		if boost_shield_two == True:
			time_boostshield_two += 1
			if time_boostshield_two > timeLimit_shield:
				boost_shield_two = False
				boostType_two.remove("shield")

		if boost_laser_one == True:
			time_boostlaser_one += 1
			if time_boostlaser_one > timeLimit_laser or laser_active_one == True:	# si le timer se termine ou si le laser est activé #
				boost_laser_one = False
				boostType_one.remove("laser")
		if boost_laser_two == True:
			time_boostlaser_two += 1
			if time_boostlaser_two > timeLimit_laser or laser_active_two == True:
				boost_laser_two = False
				boostType_two.remove("laser")


		if sprint_one == True:			# si le serpent 1 utilise le sprint #
			sprintstock_one -= 10		# il perd 10 d'endurance #
		if sprint_two == True:
			sprintstock_two -= 10

		if sprintstock_one < 0:			# si l'endurance descend en-dessous de 0 #
			sprintstock_one = 0			# elle est égale à 0 #
			sprint_one = False			# le sprint n'est plus actif #
		else:
			sprintstock_one += 1		# si l'endurance est au-dessus de 0, elle augmente de 1 #
		if sprintstock_one > sprintstock_limit:		# si l'endurance dépasse l'endurance max #
			sprintstock_one = sprintstock_limit		# endurance = 140 #

		if sprintstock_two < 0:
			sprintstock_two = 0
			sprint_two = False
		else:
			sprintstock_two += 1
		if sprintstock_two > sprintstock_limit:
			sprintstock_two = sprintstock_limit

		z = random.randrange(aleaBoost)	# z = nombre aléatoire entre 0 et 500 #
		if z == 1:					# z = 1 a une chance sur 500 d'être vraie, en sachant que la boucle se lance 15 fois par seconde #
			zis1 = True				# le boost de vitesse peut spawn #
		if z == 2:
			zis2 = True	
		if z == 3:
			zis3 = True	
		if z == 4:
			zis4 = True	

		gameDisp(lead_x_one, lead_y_one, lead_x_two, lead_y_two, randAppleX_one,randAppleY_one, randAppleX_two, randAppleY_two, zis1, zis2, zis3, zis4, boostType_one, boostType_two, sprintstock_one, sprintstock_two, boostSpeedX, boostSpeedY, boostDoubleX, boostDoubleY, boostShieldX, boostShieldY, boostLaserX, boostLaserY, boost_speed_one, boost_double_one, boost_shield_one, boost_laser_one, laser_active_one, laser_list_one, slot1_one, slot2_one, slot3_one, slot4_one, boost_speed_two, boost_double_two, boost_shield_two, boost_laser_two, laser_active_two, laser_list_two, slot1_two, slot2_two, slot3_two, slot4_two, snake_one_hide, snake_two_hide, gameOver_win_two)		

		if gameOver == True:		# si quelqu'un perd, on lance l'animation de mort #
			await animation_death(gameOver_draw, gameOver_win_two, gameOver_win_one, block_size, snakeList_one, snakeList_two, lead_x_one, lead_y_one, lead_x_two, lead_y_two, randAppleX_one,randAppleY_one, randAppleX_two, randAppleY_two, zis1, zis2, zis3, zis4, boostType_one, boostType_two, sprintstock_one, sprintstock_two, boostSpeedX, boostSpeedY, boostDoubleX, boostDoubleY, boostShieldX, boostShieldY, boostLaserX, boostLaserY, boost_speed_one, boost_double_one, boost_shield_one, boost_laser_one, laser_active_one, laser_list_one, slot1_one, slot2_one, slot3_one, slot4_one, boost_speed_two, boost_double_two, boost_shield_two, boost_laser_two, laser_active_two, laser_list_two, slot1_two, slot2_two, slot3_two, slot4_two, snake_one_hide, snake_two_hide)		
			pygame.event.clear((pygame.KEYDOWN, pygame.KEYUP))	# on oublie les touches appuyées pendant l'animation (sinon Espace met en pause ou saute l'écran de fin) #

		laser_active_one = False	# le laser ne reste activé que pendant une boucle #
		laser_active_two = False

		loopNb += 1		

		pygame.display.update()			# réactualise l'affichage #
		clock.tick(gameSpeed)
		await asyncio.sleep(0)				# la boucle while not gameExit proc speed = 15 fois par seconde #

	pygame.quit()		# si gameExit = vrai, on ferme la fenêtre #
	quit()

async def main():
	global randBg_anim
	randBg_anim = True
	await game_intro()		# lance la boucle game_intro() #
	await gameLoop()			# lance la boucle gameLoop() #

asyncio.run(main())
