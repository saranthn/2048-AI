import random
import time
from BaseAI import BaseAI
from sys import maxsize as MAX_INT
import math

class IntelligentAgent(BaseAI):

	def getMove(self, grid):
		self.time = time.process_time()
		# 3 maximize levels and 3 minimize levels
		depth = 2
		(nextState, _) = self.maximize(grid, -MAX_INT, MAX_INT, depth)
		return nextState

	def maximize(self, state, alpha, beta, depth):
		if self.terminal_test_maximize(state):
			return (None, -MAX_INT)

		(maxMove, maxUtility) = (None, -MAX_INT)

		for child in state.getAvailableMoves():
			utility = self.chance(child[1], alpha, beta, depth-1)
			if utility > maxUtility:
				maxUtility = utility
				maxMove = child[0]
			if maxUtility >= beta:
				break
			if maxUtility > alpha:
				alpha = maxUtility

		return (maxMove, maxUtility)
		pass

	def chance(self, state, alpha, beta, depth):
		return 0.1*self.minimize(state, alpha, beta, depth, 4)[1] + 0.9*self.minimize(state, alpha, beta, depth, 2)[1]
		pass

	def minimize(self, state, alpha, beta, depth, value):

		if self.terminal_test_minimize(state, depth):
			return (None, self.evaluate(state))

		(minChild,minUtility) = (None, MAX_INT)

		for emptyCell in state.getAvailableCells():
				child = state.clone()
				child.setCellValue(emptyCell, value)
				(_, utility) = self.maximize(child, alpha, beta, depth)
				if utility < minUtility:
					minUtility = utility
					minChild = child
				if minUtility <= alpha:
					break
				if minUtility < beta:
					beta = minUtility

		return (minChild, minUtility)
		pass

	def evaluate(self, state):
		emptyCells = len(state.getAvailableCells())
		# smoothness is negative. Hence it is minimized
		s = self.smoothness(state)
		return self.monotonicity(state)+s+(emptyCells**2)

	def terminal_test_maximize(self, state):
		moves = state.getAvailableMoves()
		if not moves:
			return True
		return False
		pass

	def terminal_test_minimize(self, state, depth):
		emptyCells = state.getAvailableCells()
		if not emptyCells or depth <= 0 or time.process_time()-self.time>=0.18:
			return True
		return False
		pass

	# All tiles should be in increasing order in right and down direction
	def monotonicity(self, state):
		monotonicity = 0;
		right = 0;
		for i in  range(4):
			monotonicity = 0;
			for j in range(3):
				if state.getCellValue((i,j+1)) != 0 and state.getCellValue((i,j)) <= state.getCellValue((i,j+1)):
					monotonicity += 1
					right += 4*(monotonicity ** 2)
				else:
					monotonicity = 0
					right -= (abs(state.getCellValue((i,j)) - state.getCellValue((i,j+1))))

		monotonicity = 0;
		down = 0;
		for i in  range(4):
			monotonicity = 0;
			for j in range(3):
				if state.getCellValue((j+1,i)) != 0 and state.getCellValue((j,i)) <= state.getCellValue((j+1,i)):
					monotonicity += 1
					down += 4*(monotonicity ** 2)
				else:
					monotonicity = 0
					down -= (abs(state.getCellValue((j,i)) - state.getCellValue((j+1,i))))

		return right+down
		pass

	# Minimum Difference between each tile and its neighboring tiles
	def smoothness(self, state):
		smoothness = 0;
		upDiff = MAX_INT
		downDiff = MAX_INT
		leftDiff = MAX_INT
		rightDiff = MAX_INT
		for i in  range(4):
			for j in range(4):
				current = state.getCellValue((i,j))
				up = state.getCellValue((i-1,j))
				down = state.getCellValue((i+1,j))
				left = state.getCellValue((i,j-1))
				right = state.getCellValue((i,j+1))
				if up is not None:
					upDiff = abs(current - up)
				if down is not None:
					downDiff = abs(current - down)
				if left is not None:
					leftDiff = abs(current - left)
				if right is not None:
					rightDiff = abs(current - right)
				smoothness -= min(upDiff, downDiff, leftDiff, rightDiff)
		return smoothness



	