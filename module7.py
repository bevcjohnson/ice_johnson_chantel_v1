
x = 1
j = 5

def funky(arg1, arg2):
	x = 1
	j = 5
	if arg1 > arg2:
		print('arg1 is greater than arg2')
	else:
		print('arg1 is not greater than arg2')
	print(j)

funky(x, j)

print(x)
print(j)