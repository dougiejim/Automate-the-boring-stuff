print('What is your name?')  #ask for their name
myName = input()
if myName == 'Doug':
	print('Hello Doug')
	
	print('What is the password')  #ask for their password
	password = input()
	if password == 'swordfish':
		print('Access granted.')
	else:
		print('Access denied.')

else:
	print('I do not know you, ' + myName)