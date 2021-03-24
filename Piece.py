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
		self.COLORMASK = WHITEMASK | BLACKMASK

	def isColor(self, piece, color):
		return (piece & self.COLORMASK) == color

	def Color(self, piece):
		return piece & self.COLORMASK

	def pieceType(self, piece):
		return piece & self.TYPEMASK
		
	def IsRookOrQueen(self, piece):
		return (piece & 0b110) == 0b101
		
	def IsBishopOrQueen(self, piece):
		return (piece & 0b101) == 0b101

	def isSlidingPiece(self, piece):
		return (piece & 0b100) != 0

