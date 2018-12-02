from constants import SIZE_SQUARE, BLACK, RADIUS

class Square(object):

	def getPlayer(self):
		return self._player_piece

	def setPlayer(self, valor):
		self._player_piece = valor

	def __init__(self, color, pos, t):
		self._bck_color = color
		self._pos = pos
		self._t = t
		self._player_piece = 0

		self._t.speed(0)
		self._t.pen(self._t.pen(), shown=False) # Hide Pen
		self._t.pencolor(BLACK)
		self.set_pos(pos)
		self.draw(color)

	def set_pos(self, pos):
		self._t.penup()
		self._t.setpos(pos)
		self._t.pendown()

	def draw(self, color):
		self._t.fillcolor(color)
		self._t.begin_fill()  # Shape drawn after this will be filled with this color!

		for i in range(0,4):
			self._t.forward(SIZE_SQUARE) # move forward
			self._t.left(90) # turn pen left 90 degrees

		self._t.end_fill()

	def put_piece(self,player):
		if(player == 0): return 
		self._player_piece = player
		color = 'yellow' if (player == 1) else 'royalblue'
		self.set_pos([self._pos[0]+SIZE_SQUARE/2, self._pos[1]+(SIZE_SQUARE/2-RADIUS)])
		self._t.fillcolor(color)
		self._t.begin_fill()
		self._t.circle(RADIUS)
		self._t.end_fill()
		self.set_pos(self._pos)

	def set_custom_bck(self, color):
		self.draw(color)
		if(self._player_piece != 0):
			self.put_piece(self._player_piece)

	def set_original_bck(self):
		self.draw(self._bck_color)
		if(self._player_piece != 0):
			self.put_piece(self._player_piece)

	def delete_piece(self):
		self.draw(self._bck_color)
		self._player_piece = 0