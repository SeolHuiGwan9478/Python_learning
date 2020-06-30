#순서와 컴퓨터와 사용자의 마크 출력
import random	
order = random.randrange(1,3)
if (order == 1):
	print("You will play first.")
else:
	print("I will play first.")
print("O for computer, X for you.")
for _ in range(3):
	print("+---+---+---+\n")
	print("+   +   +   +\n")
print("+---+---+---+")	

def gameboard():
	j = 0
	for i in range(3):
		print("+---+---+---+\n")
		print("+ {} + {} + {} +\n".format(matrix_list[i][j], matrix_list[i][j + 1], matrix_list[i][j + 2]))
	print("+---+---+---+")

matrix_list = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
#컴퓨터 승부 판단 함수
def judge_computer():
	if (matrix_list[0][0] == 'O' and matrix_list[1][1] == 'O' and matrix_list[2][2] == 'O'):
		truth = True
	elif (matrix_list[0][2] == 'O' and matrix_list[1][1] == 'O' and matrix_list[2][0] == 'O'):
		truth = True
	else:
		truth = False
		
	j = 0
	for i in range(3):
		if (matrix_list[i][j] == 'O' and matrix_list[i][j+1] == 'O' and matrix_list[i][j+2] == 'O') or (matrix_list[j][i] == 'O' and matrix_list[j+1][i] == 'O' and matrix_list[j+2][i] == 'O'):
			truth = True	
	return truth		
#사용자 승부 판단함수   
def judge_user():

	if (matrix_list[0][0] == 'X' and matrix_list[1][1] == 'X' and matrix_list[2][2] == 'X'):
		truth = True
	elif (matrix_list[0][2] == 'X' and matrix_list[1][1] == 'X' and matrix_list[2][0] == 'X'):		
		truth = True
	else:
		truth = False
	j = 0
	for i in range(3):
		if (matrix_list[i][j] == 'X' and matrix_list[i][j+1] == 'X' and matrix_list[i][j+2] == 'X') or (matrix_list[j][i] == 'X' and matrix_list[j+1][i] == 'X' and matrix_list[j+2][i] == 'X'):
			truth = True
	return truth		
#user turn
def user_turn():
	matrix_number = input("\n\n\nEnter a board position (row#:0..2, col#:0..2): ").split(" ")
	if (int(matrix_number[0]) != 0 and int(matrix_number[0]) != 1 and int(matrix_number[0]) != 2) or (int(matrix_number[1]) != 0 and int(matrix_number[1]) != 1 and int(matrix_number[1]) != 2):
		print("You entered a wrong position. Try again!")
		user_turn()
	else:
		x_user = int(matrix_number[0])
		y_user = int(matrix_number[1])
		if matrix_list[x_user][y_user] == 'X' or matrix_list[x_user][y_user] == 'O':
			print("You entered a wrong position. Try again!")
			user_turn()

		else:
			matrix_list[x_user][y_user] = 'X'
			gameboard()

#computer turn 함수
def computer_turn_other():
	import random
	random_list_x = []
	random_list_y = []
	for a in range(3):
		c = 0
		if matrix_list[a].count('X') == 2 and matrix_list[a].count('O') != 1:
			random_list_y.append(matrix_list[a].index(' '))
			random_list_x.append(a)
		for b in range(3):
			if matrix_list[b][a] == 'X':
				c = c + 1	
		if c == 2:
			for _ in range(3):
				if matrix_list[_][a] == ' ':
					random_list_x.append(_)
					random_list_y.append(a)
	if (matrix_list[0][0] == 'X' and matrix_list[2][2] == 'X' and matrix_list[1][1] == ' ') or (matrix_list[0][2] =='X' and matrix_list[2][0] == 'X' and matrix_list[1][1] == ' '):
		random_list_x.append(1)
		random_list_y.append(1)
	elif matrix_list[1][1] == 'X':
		if matrix_list[0][2] == 'X' and matrix_list[2][0] == ' ':
			random_list_x.append(2)
			random_list_y.append(0)
		elif matrix_list[2][0] == 'X' and matrix_list[0][2] == ' ':
			random_list_x.append(0)
			random_list_y.append(2)
		elif matrix_list[0][0] == 'X' and matrix_list[2][2] == ' ':
			random_list_x.append(2)
			random_list_y.append(2)
		elif matrix_list[2][2] == 'X' and matrix_list[0][0] == ' ':
			random_list_x.append(0)
			random_list_y.append(0)
			
	if len(random_list_x) == 0:
		while True:
			x_computer = random.randrange(3)
			y_computer = random.randrange(3)
			if matrix_list[x_computer][y_computer] != 'X' and matrix_list[x_computer][y_computer] != 'O':
				matrix_list[x_computer][y_computer] = 'O'
				break
		gameboard()	
								
	else:
		x = random.randrange(len(random_list_x))
		y = x
		x_computer = random_list_x[x]
		y_computer = random_list_y[y]
		matrix_list[x_computer][y_computer] = 'O'
		gameboard()

def computer_turn_first():
	#컴퓨터가 자기가 이기도록 설정   
	random_list_x = []
	random_list_y = []
	for a in range(3):
		c = 0
		if matrix_list[a].count('O') == 2 and matrix_list[a].count('X') != 1:
			random_list_y.append(matrix_list[a].index(' '))
			random_list_x.append(a)
		for b in range(3):
			if matrix_list[b][a] == 'O':
				c = c + 1	
		if c == 2:
			for _ in range(3):
				if matrix_list[_][a] == ' ':
					random_list_x.append(_)
					random_list_y.append(a)
	if (matrix_list[0][0] == 'O' and matrix_list[2][2] == 'O' and matrix_list[1][1] == ' ') or (matrix_list[0][2] =='O' and matrix_list[2][0] == 'O' and matrix_list[1][1] == ' '):
		random_list_x.append(1)
		random_list_y.append(1)
	elif matrix_list[1][1] == 'O':
		if matrix_list[0][2] == 'O' and matrix_list[2][0] == ' ':
			random_list_x.append(2)
			random_list_y.append(0)
		elif matrix_list[2][0] == 'O' and matrix_list[0][2] == ' ':
			random_list_x.append(0)
			random_list_y.append(2)
		elif matrix_list[0][0] == 'O' and matrix_list[2][2] == ' ':
			random_list_x.append(2)
			random_list_y.append(2)
		elif matrix_list[2][2] == 'O' and matrix_list[0][0] == ' ':
			random_list_x.append(0)
			random_list_y.append(0)
	#이길 경우의수가 없으면 사용자를 막도록 설정		
	if len(random_list_x) == 0:
		computer_turn_other()

	else:
		x = random.randrange(len(random_list_x))
		y = x
		x_computer = random_list_x[x]
		y_computer = random_list_y[y]
		matrix_list[x_computer][y_computer] = 'O'	
		gameboard()

#사용자 시작일때 경우 
if order ==	1:
	user_turn()
	print("\n")
	computer_turn_first()
	user_turn()
	print("\n")
	computer_turn_first()
	user_turn()
	print("\n")
	while True:
		if judge_user():
			print("Congratulation. You win.")
			break
		else:		
			computer_turn_first()
			if judge_computer():
				print("I win. Try again")
				break
			else:			
				user_turn()
				print("\n")
				if judge_user():
					print("Congratulation. You win.")
					break
				else:				
					computer_turn_first()
					if judge_computer():
						print("I win. Try again")
						break
					else:	
						user_turn()
						print("Draw. Try again.")
						break
#컴퓨터 시작일때 경우 	
else:
	computer_turn_first()
	user_turn()
	print("\n")
	computer_turn_first()
	user_turn()
	print("\n")
	computer_turn_first()
	while True:
		if judge_computer():
			print("I win. Try again")
			break
		else:		
			user_turn()
			print("\n")
			if judge_user():
				print("Congratulation. You win.")
				break
			else:			
				computer_turn_first()
				if judge_computer():
					print("I win. Try again")
					break
				else:				
					user_turn()
					print("\n")
					if judge_user():
						print("Congratulation. You win.")
						break
					else:	
						computer_turn_first()
						print("Draw. Try again.")
						break
	
	
