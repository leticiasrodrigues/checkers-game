from constants import SIZE_BOARD

class Game(object):

	def get_matrix(self):
		return self._m

	def init_matrix(self):
		self._m = [0] * SIZE_BOARD
		for i in range(SIZE_BOARD):
			self._m[i] = [0] * SIZE_BOARD

		for i in range(3):
			for j in range(i%2 ,SIZE_BOARD, 2):	
				self._m[i][j] = 1
				self._m[SIZE_BOARD-1-i][SIZE_BOARD-1-j] = 2