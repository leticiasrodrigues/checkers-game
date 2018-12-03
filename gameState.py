class Game_state(object):

	def __init__(self):
		self._player = 1
		self._has_selected_to_play = False
		self._steps = [] 
		self._remaining_p1 = 12
		self._remaining_p2 = 12

	def get_player(self):
		return self._player

	def set_player(self, player):
		self._player = player

	def next_player(self):
		self._player = 1 if self._player == 2 else 2
		self._has_selected_to_play = False
		self._steps= []

	def has_selected_to_play(self):
		return self._has_selected_to_play

	def add_step(self, pos):
		self._has_selected_to_play = True
		self._steps.append(pos)

	#all positions selected by player. The first is the piece to move
	def get_steps(self):
		return self._steps

	def restart_play(self, player):
		self._player = player
		self._has_selected_to_play = False
		self._steps= []

	def lost_pieces (self, n):
		if(self._player == 1):
			self._remaining_p1 = self._remaining_p1 - n
		elif(self._player == 2):
			self._remaining_p2 = self._remaining_p2 - n

	def is_game_over(self):
		if(self._remaining_p2 == 0):
			return 1
		if (self._remaining_p1 == 0):
			return 2
		return 0