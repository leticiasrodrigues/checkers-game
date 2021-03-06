import sys
from board import Board
from game import Game
from gameState import Game_state
import Tkinter
import tkMessageBox

def on_click(x, y):
	piece = b.get_index(x,y)
	i = piece[0]
	j = piece[1]

	#click outside board area
	if (i is None or j is None):
		return

	is_my_piece = g.is_my_piece(i, j, s.get_player())

	if(is_my_piece):
		#change the piece to move to current piece
		if(s.has_selected_to_play()):
			steps = s.get_steps()
			b.set_original_background(steps)
			s.restart_play()
		b.change_background(i, j, 'green')
		s.add_step(piece)
	#highlight positions where player wants to move
	elif (s.has_selected_to_play()):
			s.add_step(piece)
			b.change_background(i, j, 'yellow')
	else:
		return

#move the piece
def do_move():
	steps = s.get_steps()
	if(g.can_move_to(steps)):
		pieces_to_delete = g.play(steps)
		s.lost_pieces(len(pieces_to_delete))
		pieces_to_delete.append(steps[0])
		b.set_original_background(steps)
		b.delete_pieces(pieces_to_delete)
		i = steps[len(steps)-1][0]
		j = steps[len(steps)-1][1]
		g.change_to_checker([i,j])
		b.add_piece(i, j, g.get_player(i,j))
		s.next_player()
		winner = s.is_game_over()
		if(winner != 0):
			tkMessageBox.showinfo("We have a winner",'Player '+str(winner)+' won!')

def init_board():
	global b, g, s
	s = Game_state()
	g = Game()
	g.init_matrix()
	b = Board()
	b.set_on_click(on_click)
	b.set_play_button(do_move)
	b.set_board_state(g.get_matrix())
	b.wait()

if __name__ == "__main__":
	init_board()