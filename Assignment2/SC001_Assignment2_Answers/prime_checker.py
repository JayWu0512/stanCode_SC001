"""
File: prime_checker.py
Name:
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	input and check if the input is a prime number
	"""
	print('Welcome to the prime checker! ')
	while True:
		prime = int(input('n: '))
		if prime == EXIT:
			print('Have a good one!')
			break
		for i in range(2, prime):
			# prime can only be divided in 1 and its number.
			if prime % i == 0:
				# if the remainder is 0, it is not prime.
				print(str(prime) + ' is not a prime number.')
				break
		else:
			print(str(prime) + ' is a prime number.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
