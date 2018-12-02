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

	def is_my_piece(self, i, j, player):
		if(self._m[i][j] == player):
			return True
		return False

	#verify if the steps given represent a valid move
	def can_move_to(self,steps):
		if (len(steps)==0):
			return False

		o_i = steps[0][0]
		o_j = steps[0][1]
		p = self._m[o_i][o_j]

		#first position belongs to one player
		if(p == 0): 
			return False

		#there is at least one destination
		elif(len(steps) < 2):
			return False
		#all move positions are valid
		elif(not self.all_steps_empty(steps)):
			return False
		#take single step
		elif(len(steps) == 2 and abs(o_j - steps[1][1])==1): 
			t_i = steps[1][0]
			t_j = steps[1][1]
			if(p == 1 and t_i-o_i==1):
				return True
			if(p == 2 and o_i-t_i==1):
				return True
			return False
		#eat
		else:
			t_i = steps[1][0]
			t_j = steps[1][1]
			if(abs(o_j - t_j) != 2):
				print "Not two colluns diferent"
				return False
			if(p == 1 and t_i-o_i!=2):
				print "Not foward p1"
				return False
			if(p == 2 and o_i-t_i!=2):
				print "Not foward p2"
				return False
			#testa se posicao e valida e se tem peca no meio pra comer
			for i in range(2, len(steps)):
				if (abs(o_j - t_j) != 2 and abs(o_i - t_i) != 2):
					return False
				if(self._m[t_i][t_j] != 0): #square not empty
					return False
				#there is a piece in the middle and its an adversary piece
				adv_player = 1 if p == 2 else 2
				if(self._m[(o_i + t_i)/2][(o_j + t_j)/2] == adv_player):
					o_j = t_i
					o_j = t_j
					t_i = steps[i][0]
					t_j = steps[i][1]
					continue
				else:
					return False
			return True

	def all_steps_empty(self, steps):
		steps = steps[1:]
		for s in steps:
			if(self._m[s[0]][s[1]] != 0):
				return False
		return True

	#change matrix to represent the moves given by steps
	#assumes that steps represent a valid move
	def play(self, steps):
		pieces_to_delete = []
		l = len(steps)
		player = self._m[steps[0][0]][steps[0][1]]
		self._m[steps[0][0]][steps[0][1]] = 0
		self._m[steps[l-1][0]][steps[l-1][1]] = player
		if(l >= 2 and abs(steps[0][1] - steps[1][1])==2):
			for k in range(l-1):
				p0 = steps[k]
				p1 = steps[k+1]
				self._m[(p0[0] + p1[0])/2][(p0[1] + p1[1])/2] = 0
				pieces_to_delete.append([(p0[0] + p1[0])/2,(p0[1] + p1[1])/2 ])
		return pieces_to_delete

