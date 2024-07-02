
place_holders = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
#                 0   1   2   3   4   5   6   7   8
moves = 0

carti = {
	'11': 0,
	'12': 1,
	'13': 2,
	'21': 3,
	'22': 4,
	'23': 5,
	'31': 6,
	'32': 7,
	'33': 8
}

def exe():
	k=0
	for i in range(3):
		for j in range(3):
			print(f" {place_holders[k]}",end='')
			if j != 2:
				print(" | ",end='')
			k+=1
		if i != 2:
			print("\n--------------")

def is_ther_winner():
	print("\n")
	if  place_holders[carti['11']]== "O" and place_holders[carti['12']] == "O" and place_holders[carti['13']] == "O":
		print('O is the Winner!')
		return True

	elif  place_holders[carti['21']]== "O" and place_holders[carti['22']] == "O" and place_holders[carti['23']] == "O":
		print('O is the Winner!')
		return True
	
	elif  place_holders[carti['31']]== "O" and place_holders[carti['32']] == "O" and place_holders[carti['33']] == "O":
		print('O is the Winner!')
		return True

	elif  place_holders[carti['11']]== "O" and place_holders[carti['22']] == "O" and place_holders[carti['33']] == "O":
		print('O is the Winner!')
		return True
	
	elif  place_holders[carti['13']]== "O" and place_holders[carti['22']] == "O" and place_holders[carti['31']] == "O":
		print('O is the Winner!')
		return True

	elif  place_holders[carti['11']]== "O" and place_holders[carti['21']] == "O" and place_holders[carti['31']] == "O":
		print('O is the Winner!')
		return True

	elif  place_holders[carti['12']]== "O" and place_holders[carti['22']] == "O" and place_holders[carti['32']] == "O":
		print('O is the Winner!')
		return True

	elif  place_holders[carti['13']]== "O" and place_holders[carti['23']] == "O" and place_holders[carti['33']] == "O":
		print('O is the Winner!')
		return True
	
	elif  place_holders[carti['11']]== "X" and place_holders[carti['12']] == "X" and place_holders[carti['13']] == "X":
		print('X is the Winner!')
		return True
	
	elif  place_holders[carti['21']]== "X" and place_holders[carti['22']] == "X" and place_holders[carti['23']] == "X":
		print('X is the Winner!')
		return True
	
	elif  place_holders[carti['31']]== "X" and place_holders[carti['32']] == "X" and place_holders[carti['33']] == "X":
		print('X is the Winner!')
		return True

	elif  place_holders[carti['11']]== "X" and place_holders[carti['22']] == "X" and place_holders[carti['33']] == "X":
		print('X is the Winner!')
		return True
	
	elif  place_holders[carti['13']]== "X" and place_holders[carti['22']] == "X" and place_holders[carti['31']] == "X":
		print('X is the Winner!')
		return True

	elif  place_holders[carti['11']]== "X" and place_holders[carti['21']] == "X" and place_holders[carti['31']] == "X":
		print('X is the Winner!')
		return True

	elif  place_holders[carti['12']]== "X" and place_holders[carti['22']] == "X" and place_holders[carti['32']] == "X":
		print('X is the Winner!')
		return True

	elif  place_holders[carti['13']]== "X" and place_holders[carti['23']] == "X" and place_holders[carti['33']] == "X":
		print('X is the Winner!')
		return True
	

exe()

for i in range(9):
	if is_ther_winner():
		is_ther_winner()
		break
	
	if moves%2==0:
		mover = "O"
		moves+=1
	else:
		mover = "X"
		moves+=1
	position = str(input("\nEnter the row and column(11): "))
	try:
		place_holders[carti[position]] = mover
	except KeyError:
		print("Invalid Position")
		continue
	print("\n\n")
	exe()
