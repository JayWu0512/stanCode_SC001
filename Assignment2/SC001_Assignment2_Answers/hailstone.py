"""
File: hailstone.py
Name:
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    : param a : int, the number to be typed in hailstone.
    : param count : int, count how many steps in hailstone.
    """
    print('This program computes Hailstone sequences. ')
    a = int(input("Enter a number: "))
    if a == 1:
        print('It took 0 step to reach 1.')
    # boundary condition
    else:
        count = 0
        # start with o step
        while a != 1:
            if a % 2 == 1:
                # odd number
                b = 3*a + 1
                print(str(a)+' is odd, so I make 3n+1: ' + str(b))
                a = b
                count += 1
            elif a % 2 == 0:
                # even number
                c = a/2
                print(str(a) + ' is even, so I take half: ' + str(c))
                a = c
                count += 1
        print('It took ' + str(count) + ' steps to reach 1.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
