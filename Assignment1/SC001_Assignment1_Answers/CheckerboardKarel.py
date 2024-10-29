"""
File: CheckerboardKarel.py
Name: 
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at (1,1), facing East.
    post-condition: Karel is on the topmost of the checkerboard.
    """
    while front_is_clear():
        fill_odd_street()
        # for the topmost street
        if left_is_clear():
            fill_even_street()
    # for (8,1) checkerboard
    turn_left()
    while front_is_clear():
        fill_odd_street()
        fill_even_street()


def fill_odd_street():
    """
    pre-condition: Karel is at the start of odd street, facing East.
    post-condition: Karel is at the start of even street, facing West.
    """
    # start with a beeper
    put_beeper()
    move()
    # move to the end
    while front_is_clear():
        move()
        if front_is_clear():
            put_beeper()
            move()
        else:
            put_beeper()
    # for the topmost street
    if left_is_clear():
        start_the_even_street()


def fill_even_street():
    """
    pre-condition: Karel is at the start of even street, facing West.
    post-condition: Karel is at the start of odd street, facing East.
    """
    while front_is_clear():
        move()
        # move to the end
        if front_is_clear():
            move()
            put_beeper()
    start_the_odd_street()


def start_the_even_street():
    """
    pre-condition: Karel is at the end of odd street, facing East.
    post-condition: Karel is at the start of even street, facing West.
    """
    # for 8x8
    if not on_beeper():
        move_to_even_street()
        put_beeper()
    # for 7x7
    else:
        move_to_even_street()
        move()
        put_beeper()


def start_the_odd_street():
    """
    pre-condition: Karel is at the end of even street, facing West.
    post-condition: Karel is at the start of odd street, facing East.
    """
    # for 8x8
    if not on_beeper():
        move_to_odd_street()
    # for 7x7
    else:
        move_to_odd_street()
        move()


def move_to_even_street():
    """
    pre-condition: Karel is at the end of odd street, facing East.
    post-condition: Karel is at the start of even street, facing West.
    """
    turn_left()
    if front_is_clear():
        move()
        turn_left()


def move_to_odd_street():
    """
    pre-condition: Karel is at the end of even street, facing West.
    post-condition: Karel is at the start of odd street, facing East.
    """
    turn_right()
    if front_is_clear():
        move()
        turn_right()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
