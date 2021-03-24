import pygame
from Coord import *

class GUIBoard:
	def __init__(self, darkColor, lightColor, size):
		self.surface = pygame.Surface((size, size))
		self.colors = (darkColor, lightColor)
		self.Coords = [Coord(j) if j==0 else Coord(j) for j in range(0,64)]
		self.size = (size, size)
		self.sqSize = size/8

	def drawSquares(self, All=True, index=0):
		if All:
			for file in range(8):
				for rank in range(8):
					pygame.draw.rect(self.surface, 
						self.colors[1] if self.Coords[(file*8)+rank].isLightSquare else self.colors[0],
						pygame.Rect(file*self.sqSize, rank*self.sqSize, self.sqSize, self.sqSize))

	def draw(self, surface):
		self.drawSquares()
		surface.blit(self.surface, (0,0))
