"""
File: quadratic_solver.py
Name:
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	: param a : int, the first number to be inputted.
	: param b : int, the second number to be inputted.
	: param c : int, the third number to be inputted.
	: param d : discriminant formula
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	d = b * b - 4 * a * c
	if d < 0:
		print('No real roots ')
	elif d > 0:
		quadratic_1 = (-b + math.sqrt(d)) / 2 * a
		quadratic_2 = (-b - math.sqrt(d)) / 2 * a
		print('Two roots: ' + str(quadratic_1) + ' , ' + str(quadratic_2))
	elif d == 0:
		quadratic_1 = (-b + math.sqrt(d)) / 2 * a
		print('One root: ' + str(quadratic_1))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
