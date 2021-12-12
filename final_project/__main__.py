"""
Description for this class.

OOP Principles Used:
Abstraction
Encapsulation
Inheritance 
Polymorphism - Ongoing...

Reasoning:
This program uses abstraction, since the whole program was broken into smaller pieces/classes
This program uses encapsulation, since the all constant variables are private since they don't need to be changed
This program uses inheritance because music.py invokes a super class constructor that, initializes points to zero, sets the positions, and plays the music
This file uses polymorphism because ...
"""
import arcade
from zombiekiller import constants, menu

def main():
    """ Main method """
    window = arcade.Window(constants._SCREEN_WIDTH, constants._SCREEN_HEIGHT, constants._SCREEN_TITLE)
    __start_view = menu.MenuView()
    window.show_view(__start_view)
    arcade.run()

if __name__ == "__main__":
    main()