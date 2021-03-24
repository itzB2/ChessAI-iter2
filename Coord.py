class Coord:
	def __init__(self, index):
		self._file = int(index % 8)
		self._rank = int(index / 8)
		self._selected = False

	@property
	def file(self):
		return self._file

	@property
	def rank(self):
		return self._rank

	@property
	def selected(self):
		return self._selected

	@property
	def isLightSquare(self):
		return (self._file + self._rank) % 2 != 0

	def Compare(self, other):
		return 1 if (self._file == other.file and self._rank == other.rank) else 0