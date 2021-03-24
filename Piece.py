import pygame as pg
import os

Lookup = {0:"None", 1:"King", 2:"Pawn", 3:"Knight", 5:"Bishop", 6:"Rook", 7:"Queen", 8:"White", 16:"Black"}

p = {"White King":pg.image.load(os.path.join("Sprites", "White King.png")).convert_alpha(),
	 "White Queen":pg.image.load(os.path.join("Sprites", "White Queen.png")).convert_alpha(),
	 "White Bishop":pg.image.load(os.path.join("Sprites", "White Bishop.png")).convert_alpha(),
	 "White Knight":pg.image.load(os.path.join("Sprites", "White Knight.png")).convert_alpha(),
	 "White Rook":pg.image.load(os.path.join("Sprites", "White Rook.png")).convert_alpha(),
	 "White Pawn":pg.image.load(os.path.join("Sprites", "White Pawn.png")).convert_alpha(),
	 "Black King":pg.image.load(os.path.join("Sprites", "Black King.png")).convert_alpha(),
	 "Black Queen":pg.image.load(os.path.join("Sprites", "Black Queen.png")).convert_alpha(),
	 "Black Bishop":pg.image.load(os.path.join("Sprites", "Black Bishop.png")).convert_alpha(),
	 "Black Knight":pg.image.load(os.path.join("Sprites", "Black Knight.png")).convert_alpha(),
	 "Black Rook":pg.image.load(os.path.join("Sprites", "Black Rook.png")).convert_alpha(),
	 "Black Pawn":pg.image.load(os.path.join("Sprites", "Black Pawn.png")).convert_alpha(),
	 "Blank":pg.image.load(os.path.join("Sprites", "blank.png")).convert_alpha()
	}

class Piece:
	def __init__(self):
		self.NONE = 0
		self.KING = 1
		self.PAWN = 2
		self.KNIGHT = 3
		self.BISHOP = 5
		self.ROOK = 6
		self.QUEEN = 7

		self.WHITE = 8
		self.BLACK = 16

		self.TYPEMASK = 0b00111
		self.BLACKMASK = 0b10000
		self.WHITEMASK = 0b01000
		self.COLORMASK = self.WHITEMASK | self.BLACKMASK

	def isColor(self, piece, color):
		return (piece & self.COLORMASK) == color

	def Color(self, piece, name = False):
		return Lookup[piece & self.COLORMASK] if name else (piece & self.COLORMASK)

	def pieceType(self, piece, name = False):
		return Lookup[piece & self.TYPEMASK] if name else (piece & self.TYPEMASK)

	def getSprite(self, piece):
		pieceType = self.pieceType(piece, True)
		color = self.Color(piece, True)
		
	def IsRookOrQueen(self, piece):
		return (piece & 0b110) == 0b101
		
	def IsBishopOrQueen(self, piece):
		return (piece & 0b101) == 0b101

	def isSlidingPiece(self, piece):
		return (piece & 0b100) != 0

