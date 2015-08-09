import pygame
import sys

from stuff import main
from stuff import values

x, y = values.map_x*12, values.map_y*8
if x < 60:
	x = 60
if y < 88:
	y = 88
pygame.init()
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Dogs & Sheeps")
pygame.display.init()
#pygame.display.set_icon(pygame.image.load("pic/corpse.png")) #Later, I don't want to do it now...
bg_color=(0,0,0)

def cGroup(picnames, placex = x/2, placey = y/2):
	buttons = pygame.sprite.Group()
	for picname in picnames:
		button = pygame.sprite.Sprite()
		button.name = picname
		button.image = pygame.image.load("stuff/pic/" + picname + ".PNG").convert_alpha()
		button.rect = button.image.get_rect()
		button.rect.center = (x/2, placey)
		placey += 20
		buttons.add(button)
	return buttons

picnames = ["Play", "Options", "Button3", "Quit"]
placey = y/2 - 10 * (len(picnames) - 1) - 8
if y == 88:
	placey  += 8
buttons_main = cGroup(picnames, placey = placey)

myfile = open("stuff/values.py", "r")
lines = myfile.read().split("\n")

while True:
	for event in pygame.event.get():
		if pygame.mouse.get_pressed()[0]:
			pos = pygame.mouse.get_pos()
			for button in buttons_main:
				if button.rect.left < pos[0] and button.rect.right > pos[0] and button.rect.top < pos[1] and button.rect.bottom > pos[1]:
					print(button.name)
					if button.name == "Play":
						main.Run()
					elif button.name == "Options":
						print(button.name)
					elif button.name == "Quit":
						sys.exit()
		elif event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			#print("Thanks for using!")
			#sleep(2)
			sys.exit()
	buttons_main.draw(screen)
	pygame.display.update()
