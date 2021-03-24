from Piece import *

Piece = Piece()

def decodeFen(fen, board):
	typeLookup = {'k':Piece.KING,'p':Piece.PAWN,'n':Piece.KNIGHT,'b':Piece.BISHOP,'r':Piece.ROOK,'q':Piece.QUEEN}
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
				pieceColor = Piece.WHITE if char.isupper() else Piece.BLACK
				pieceType = typeLookup[char.lower()]
				board.setPiece((file * 8) + rank, pieceType | pieceColor)
				file+=1

class Board:
	def __init__(self, guiBoard,  fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
		self.fen = fen
		self.pieces = [Piece.NONE if j==0 else Piece.NONE for j in range(0,64)]
		self.GUIBoard = guiBoard

	def setPiece(self, index, piece):
		self.pieces[index] = piece

