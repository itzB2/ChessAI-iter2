#Libraries
import pygame

pygame.init()

#Own Modules
from UI import *
from Board import Board
from Piece import *

DISPLAY = pygame.display.set_mode((720,720))

size = DISPLAY.get_width()
dC = (255, 137, 94)
lC = (200,200,200)

GUIboard = GUIBoard(dC,lC,size)
Board = Board(GUIBoard)
GUIboard.setLogicBoard(Board)

running = False
while not running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = True
		# elif event.type == pygame.MOUSEBUTTONDOWN:
		# 	mPos = pygame.mouse.get_pos()
		# 	if pygame.mouse.get_pressed()[0] == 1:
		# 		board.selectSquare(mPos)
		# 	elif pygame.mouse.get_pressed()[1] == 1:
		# 		#MIDDLE
		# 		pass
		# 	elif pygame.mouse.get_pressed()[2] == 1:
		# 		#RMB
		# 		pass

	GUIboard.draw(DISPLAY)
	pygame.display.update()