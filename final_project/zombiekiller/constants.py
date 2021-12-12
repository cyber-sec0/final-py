"""
Description for this class.

OOP Principles Used:
Abstraction
Encapsulation

Reasoning:
This class uses abstraction, since the it is a class that helps the whole program be broken into smaller pieces/classes
This class uses encapsulation, since  all constant variables are private since they don't need to be changed
"""

from pathlib import Path

home = Path.home()
assets: Path = Path(__file__).parent / 'assets'

_MAIN_MUSIC = assets / 'Scary Creepy Psycho Music.mp3'
_DEFAULT_VOLUME = .15
_SCREEN_WIDTH = 1280
_SCREEN_HEIGHT = 700
_CHARACTER_SCALING = 1
_PLAYER_MOVEMENT_SPEED = 5
_SCREEN_TITLE = "THE BEST ZOMBIE KILLER GAME EVER!!!"