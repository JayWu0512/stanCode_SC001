"""
File: StoneMasonKarel.py
Name: 
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at the left side, facing East.
    post-condition: Karel is at the right side, facing East. All columns are constructed.
    """
    while front_is_clear():
        build_the_column()
        move_to_the_next_column()
    # for the last column
    build_the_column()


def build_the_column():
    """
    pre-condition: Karel is at bottom of a column, facing East.
    post-condition: Karel finishes building a column, facing East.
    """
    turn_left()
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    if not on_beeper():
        put_beeper()
    turn_around()
    for i in range(4):
        move()
    turn_left()


def move_to_the_next_column():
    """
    pre-condition: Karel is at bottom of a column, facing East.
    post-condition: Karel moves to the next column, facing East.
    """
    for i in range(4):
        move()


def turn_around():
    """
    pre-condition: Karel is facing North.
    post-condition: Karel is facing South.
    """
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
