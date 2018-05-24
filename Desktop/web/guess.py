print('\nThink about a number between 0 - 100 and let me guess which is it.',
'\n\nI will ask you whether my guess is lower or higher than your number',
'\nIndicate "l" if lower than your number',
'"h" if higher than your number and',
'"e" if my guess is correct.'
'\n\nAre you ready?, let"s start!\n')

# Algorithm
count = 0
lborder = 0
hborder = 100
guess = 50

while True:
	answer = input('Is your number higher, lower or equal to ' + str(guess) + ':')
	if answer == 'l':	
		hborder = guess
		guess = round((lborder + guess)/2)
	elif answer == 'h':
		lborder = guess
		guess = round((hborder + guess) / 2)
	elif answer == 'e':
		break
	else:
		print('Unrecognizable answer. Use: "l", "h", "e"')
	count += 1

print('\nHooray! It took me', count, 'to guess your number.', sep=' ')
input('\nPress Enter to Exit.')
file = open("input.txt","r")
a = file.read()
file.close()
a = a.split()
sum = int(a[0]) + int(a[1])
file = open("output.txt","w")
file.write(str(sum))
file.close()