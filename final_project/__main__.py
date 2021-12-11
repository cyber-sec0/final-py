"""
Abstraction - This program uses abstraction, since the whole program was broken into smaller pieces/classes
Encapsulation - This program uses encapsulation, since the all constant variables are private since they don't need to be changed
Inheritance - music.py invokes a super class constructor that, initializes points to zero, sets the positions, and plays the music 
Polymorphism - 

polymorphism makes the program be scattered into multiple parts containing all functions, logic, conditions,
 operations and data necessary to perform an action
 
 with polymorphism we summarize all of it in a single line containing a call to perform all these actions. 
 So it's easier and faster to see what that single line of code is doing.
polymorphism can also override classes
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