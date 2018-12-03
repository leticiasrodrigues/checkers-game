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
		if(self._m[i][j]%10 == player):
			return True
		return False

	def get_player(self, i, j):
		return self._m[i][j]

	#verify if the steps given represent a valid move
	def can_move_to(self,steps):
		if (len(steps)==0):
			return False
		p = self._m[steps[0][0]][steps[0][1]]

		#first position belongs to one player
		if(p == 0): 
			return False
		#there is at least one destination
		elif(len(steps) < 2):
			return False
		#all positions to move are empty
		elif(not self.all_steps_empty(steps)):
			return False
		#checker move
		elif(p > 10):
			return self.can_checker_move_to(steps)
		#simple move
		else:
			return self.can_simple_move_to(steps)
		
	def can_simple_move_to(self, steps):
		o_i = steps[0][0]
		o_j = steps[0][1]
		p = self._m[o_i][o_j]
		adv_player = 1 if p == 2 else 2
		#take single step	
		if(len(steps) == 2 and abs(o_j - steps[1][1])==1): 
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
				return False
			#verify if pieces are moving foward
			if(p == 1 and t_i-o_i!=2):
				return False
			if(p == 2 and o_i-t_i!=2):
				return False
			#eat one piece
			if(len(steps)==2):
				if(self._m[(o_i + t_i)/2][(o_j + t_j)/2] != adv_player):
					return False
				else:
					return True
			#eat several pieces
			#verify if its a valid move and if the piece in the middle belongs to adversary
			for i in range(2, len(steps)):
				if (abs(o_j - t_j) != 2 and abs(o_i - t_i) != 2):
					return False #not a valid move
				if(self._m[t_i][t_j] != 0): #square not empty
					return False
				#there is a piece in the middle and its an adversary piece
				if(self._m[(o_i + t_i)/2][(o_j + t_j)/2] == adv_player):
					o_j = t_i
					o_j = t_j
					t_i = steps[i][0]
					t_j = steps[i][1]
					continue
				else:
					return False
			return True

	def can_checker_move_to(self, steps):
		a = steps[0]
		p = self._m[a[0]][a[1]]%10
		adv_p = 2 if p == 1 else 1
		find_adv = False

		for s in steps[1:]:
			if(abs(a[0] - s[0]) != abs(a[1] - s[1])) :
				return False #not a diagonal
			diag = self.return_diag(a,s)
			for d in diag:
				v = self._m[d[0]][d[1]]%10
				if (v == 0):
					continue
				if(v == p):
					return False
				if(v == adv_p and not find_adv):
					find_adv = True
					continue
				if(v == adv_p and find_adv):
					return False
			find_adv = False
			a = s
		return True

	def return_diag(self, a, b):
		diag = []
		i = range(a[0], b[0]) if a[0] < b[0] else range(a[0], b[0], -1)
		j = range(a[1], b[1]) if a[1] < b[1] else range(a[1], b[1], -1)
		diff = abs(a[0] - b[0])
		for k in range(1,diff):
			diag.append([i[k],j[k]])
		return diag

	def all_steps_empty(self, steps):
		steps = steps[1:]
		for s in steps:
			if(self._m[s[0]][s[1]] != 0):
				return False
		return True

	#change matrix to represent the moves given by steps
	#assumes that steps represent a valid move
	def play(self, steps):
		l = len(steps)
		player = self._m[steps[0][0]][steps[0][1]]
		self._m[steps[0][0]][steps[0][1]] = 0
		self._m[steps[l-1][0]][steps[l-1][1]] = player
		if(player > 10):
			return self.checker_move(steps)
		else:
			return self.simple_move(steps)
		

	def simple_move(self, steps):
		pieces_to_delete = []
		l = len(steps)
		if(l >= 2 and abs(steps[0][1] - steps[1][1])==2):
			for k in range(l-1):
				p0 = steps[k]
				p1 = steps[k+1]
				self._m[(p0[0] + p1[0])/2][(p0[1] + p1[1])/2] = 0
				pieces_to_delete.append([(p0[0] + p1[0])/2,(p0[1] + p1[1])/2 ])
		return pieces_to_delete


	def checker_move(self, steps):
		pieces_to_delete = []
		s0 = steps[0]
		for s in steps[1:]:
			diag = self.return_diag(s0, s)
			for d in diag:
				if(self._m[d[0]][d[1]] != 0):
					self._m[d[0]][d[1]] = 0
					pieces_to_delete.append(d)
					break
			s0 = s
		return pieces_to_delete

	def change_to_checker(self, pos):
		p = self._m[pos[0]][pos[1]]
		if((p == 1 and pos[0] == 7) or (p == 2 and pos[0] == 0)):
			self._m[pos[0]][pos[1]] = p+10
			return True
		return False

