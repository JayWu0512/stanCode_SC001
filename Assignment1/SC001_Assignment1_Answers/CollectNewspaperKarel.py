"""
File: CollectNewspaperKarel.py
Name: 
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is in the upper left corner of the house, with nothing on its hand.
    post-condition: Karel returns to its initial position, with newspaper on its hand.
    """
    move_to_newspaper()
    back_to_home()


def move_to_newspaper():
    """
    pre-condition: Karel is in the upper left corner of the house, with nothing on its hand.
    post-condition: Karel takes the newspaper, facing East.
    """
    turn_right()
    move()
    turn_left()
    for i in range(3):
        move()
    pick_beeper()


def back_to_home():
    """
    pre-condition: Karel takes the newspaper, facing East.
    post-condition: Karel returns to its initial position, with a newspaper on its hand.
    """
    turn_around()
    for i in range(3):
        move()
    turn_right()
    move()
    turn_right()
    put_beeper()


def turn_right():
    """
    This function turns Karel to the left three times.
    """
    for i in range(3):
        turn_left()


def turn_around():
    """
    This function turns Karel to the left two times.
    """
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
