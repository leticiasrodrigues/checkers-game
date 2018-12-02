import sys
from board import Board
from game import Game
from gameState import Game_state

def on_click(x, y):
	piece = b.get_index(x,y)
	i = piece[0]
	j = piece[1]

	if (i is None or j is None):
		return

	is_my_piece = g.is_my_piece(i, j, s.get_player())

def init_board():
	global b, g, s
	s = Game_state()
	g = Game()
	g.init_matrix()
	b = Board()
	b.set_on_click(on_click)
	b.set_board_state(g.get_matrix())
	b.wait()

if __name__ == "__main__":
	init_board()