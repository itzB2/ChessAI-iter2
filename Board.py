from Piece import *

def decodeFen(fen, board):
	typeLookup = {'k':"King",'p':"Pawn",'n':"Knight",'b':"Bishop",'r':"Rook",'q':"Queen"}
	fenBoard = fen.split(" ")[0]
	file = 0
	rank = 7

	for char in fenBoard:
		if char =="/":
			file = 0
			rank -=1
		else:
			if char.isdigit():
				file += int(char)
			else:
				pieceColor = "White" if char.isupper() else "Black"
				pieceType = typeLookup[char.lower()]
				self.pieces[file][rank] = Piece(pieceColor, pieceType)
				file+=1

class Board:
	def __init__(self, fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
		self.fen = fen

	def 