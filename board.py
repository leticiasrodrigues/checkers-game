from square import Square
import turtle
from constants import SIZE_BOARD, BLACK, WHITE, SIZE_SQUARE, START, BKG_COLOR

class Board (object):

	def __init__(self):
		self._screen = turtle.Screen()
		self._screen.bgcolor(BKG_COLOR)
		self.create_board()

	def wait(self):
		turtle.done()

	def set_on_click(self, func):
		self._screen.onclick(func)
		self._screen.listen()

	def set_board_state(self, m):
		for i in range(SIZE_BOARD):
			for j in range(SIZE_BOARD):
				self._m[i][j].put_piece(m[i][j])

	def create_board(self):
		self._m = [] * SIZE_BOARD
		color = BLACK
		for i in range(SIZE_BOARD):
			mi = [] * SIZE_BOARD
			for j in range(SIZE_BOARD):
				s = Square(color, [self.pos_from_index(i), self.pos_from_index(j)],turtle.Turtle())
				mi.insert(j, s)
				color = WHITE if (color==BLACK) else BLACK
			self._m.insert(i,mi)
			color = WHITE if (color==BLACK) else BLACK

	def pos_from_index(self,i):
		return START+(i*SIZE_SQUARE)
