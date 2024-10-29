"""
File: rocket.py
Name:
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    step 1: build a rocket head
    step 2: build a rocket belt
    step 3: build rocket's upper body
    step 4: build rocket's lower body
    step 5: as same as step 2
    step 6: as same as step 1
    """
    build_head()
    build_belt()
    build_upper()
    build_lower()
    build_belt()
    build_head()


def build_head():
    for i in range(SIZE):
        for j in range(SIZE-i):
            # 3 to 2 to 1
            print(' ', end='')
        for j in range(i+1):
            # 1 to 2 to 3
            print('/', end='')
        for j in range(i+1):
            print('\\', end='')
        print('')


def build_belt():
    print('+', end='')
    for i in range(SIZE * 2):
        print('=', end='')
    print('+')


def build_upper():
    for i in range(SIZE):
        print('|', end='')
        for j in range(SIZE-i-1):
            # 2 to 1 to 0
            print('.', end='')
        for j in range(i+1):
            # 1 to 2 to 3
            print('/'+'\\', end='')
        for j in range(SIZE-i-1):
            print('.', end='')
        print('|')
    print('', end='')


def build_lower():
    for i in range(SIZE):
        print('|', end='')
        for j in range(i):
            # 0 to 1 to 2
            print('.', end='')
        for j in range(SIZE-i):
            # 3 to 2 to 1
            print('\\'+'/', end='')
        for j in range(i):
            print('.', end='')
        print('|')
    print('', end='')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
