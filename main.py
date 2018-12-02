import sys
from board import Board
from game import Game

def on_click(x, y):
	pass

def init_board():
	global b, g
	g = Game()
	g.init_matrix()
	b = Board()
	b.set_on_click(on_click)
	b.set_board_state(g.get_matrix())
	b.wait()

if __name__ == "__main__":
	init_board()