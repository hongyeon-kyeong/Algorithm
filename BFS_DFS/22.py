from collections import deque

def get_next_post(pos, board) :
	dx = [1,-1,0,0]
	dy = [0,0,-1,1]
	pos = list(pos)
	next_pos = []

	pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

	for i in range(4) :
		next_pos1_x, next_pos1_y, next_pos2_x, next_pos2_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]

		if board[next_pos1_x][next_pos1_y] == 0 and board[next_pos2_x][next_pos2_y] == 0 :
			next_pos.append({(next_pos1_x, next_pos1_y),(next_pos2_x, next_pos2_y)})
	
	if pos1_x == pos2_x :
		for i in [1,-1] :
			if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0 :
				next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
				next_pos.append({(pos2_x, pos2_y), (pos2_x+i, pos2_y)})		

	elif pos1_y == pos2_y :
		for i in [-1,1] :
			if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y+i] == 0 :
				next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
				next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
	return next_pos

def solution(board) :
	n = len(board)
	new_board = [[1] * (n+2) for _ in range(n+2)]

	for i in range(n) :
		for j in range(n) :
			new_board[i+1][j+1] = board[i][j]
	
	q = deque()
	pos = {(1,1),(1,2)}
	q.append((pos,0))
	visited = []
	visited.append(pos)

	while q :
		pos, cost = q.popleft()

		if (n,n) in pos :
			return cost
		
		for next_pos in get_next_post(pos, new_board) :
			if next_pos not in visited :
				q.append((next_pos, cost+1))
				visited.append(next_pos)
	return 0

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))