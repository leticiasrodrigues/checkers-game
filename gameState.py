class Game_state(object):

	def __init__(self):
		self._player = 1

	def get_player(self):
		return self._player

	def set_player(self, player):
		self._player = player

	def next_player(self):
		self._player = 1 if self._player == 2 else 2