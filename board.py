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

	def set_play_button(self, func):
		self._screen.onkey(func, "Return")

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

	def index_from_pos(self, x):
		for i in list(range(SIZE_BOARD)):
			if( x >= (self.pos_from_index(i)) and x < (self.pos_from_index(i)) + SIZE_SQUARE):
				return i

	def get_index(self, x, y):
		i = self.index_from_pos(x)
		j = self.index_from_pos(y)
		return [i,j]

	def set_original_background(self, squares):
		for s in squares:
			self._m[s[0]][s[1]].set_original_bck();

	def change_background(self, i, j, color):
		self._m[i][j].set_custom_bck(color)

	def delete_pieces(self, pieces):
		for k in pieces:
			self._m[k[0]][k[1]].delete_piece()

	def add_piece(self, i,j,player):
		self._m[i][j].put_piece(player)
		self._m[i][j].set_original_bck();

