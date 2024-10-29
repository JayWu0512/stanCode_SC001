"""
File: MidpointKarel.py
Name: 
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    pre_condition: Karel is at (1,1), facing East.
    post-condition: Karel is at the middle of the world.
    """
    # use beeper to count, fill a street without the street near wall.
    fill_the_line()
    find_the_nearest_beeper()
    # pick the beeper near wall, so Karel can start a loop.
    walk_to_the_start()
    find_the_nearest_beeper()
    # beepers near walls are picked, so a loop can start.
    while on_beeper():
        walk_to_the_last_beeper()
        take_the_first_beeper()
    # beepers are all picked, so Karel goes to the middle of the street.
    walk_to_the_last_beeper()
    put_beeper()


def fill_the_line():
    """
    pre-condition: Karel is at (1,1), facing East.
    post-condition: Karel is at the end of the beeper, but it is not on beeper.
    """
    while front_is_clear():
        if not on_beeper():
            put_beeper()
            move()


def find_the_nearest_beeper():
    """
    pre-condition: Karel is at the end of the beeper, but it is not on beeper.
    post-condition: Karel is at the end of the beeper, and it is on beeper.
    """
    turn_around()
    move()


def walk_to_the_start():
    """
    pre-condition: Karel is at the end of the beeper, and it is on beeper.
    post-condition: Karel is at the start of the beeper, but it is not on beeper.
    """
    while on_beeper():
        if front_is_clear():
            move()
        else:
            pick_beeper()


def walk_to_the_last_beeper():
    """
    pre-condition: Karel is at the start of the beeper, but it is not on beeper.
    post-condition: Karel walks to the farthest beeper, and a beeper next to it.
    """
    while on_beeper():
        move()
    find_the_nearest_beeper()


def take_the_first_beeper():
    """
    pre-condition: Karel is next to a beeper.
    post-condition: Karel takes a beeper next to it.
    """
    pick_beeper()
    move()


def turn_around():
    """
    Karel turn left two times.
    """
    for i in range(2):
        turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
