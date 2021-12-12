"""
Description for this class.

OOP Principles Used:
Abstraction
Encapsulation
Inheritance 

Reasoning:
This class uses abstraction, since the it is a class that helps the whole program be broken into smaller pieces/classes
This class uses encapsulation, since the __score_text constant variable is private since it don't need to be changed
This class uses inheritance because music.py invokes a super class constructor that, initializes points to zero, sets the positions, and plays the music
"""
import arcade, random
from zombiekiller import constants, draw

class MyGame(arcade.View):
    """
    Main application class.
    """

    def __init__(self, player_sprite, computer_list):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the positions,
        and plays the music.
        """

        # Call the parent class and set up the window
        # super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        super().__init__()
        self.master_volume = constants._DEFAULT_VOLUME
        self.background_music = arcade.Sound(constants._MAIN_MUSIC)
        self.background_music.play(self.master_volume, loop = True)

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.computer_list = None
        self.player_list = None
        self.score = 0

        # Separate variable that holds the player sprite
        self.player_sprite = None

        arcade.set_background_color(arcade.csscolor.DARK_SEA_GREEN)

    def generate_enemy(self, delta_time):
        # Add a computer zombie on the side of the screen
        enemy_size = self.player_sprite._get_scale() - 0.5 + random.random()
        wall = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_fall.png", enemy_size)
        wall.position = [constants._SCREEN_WIDTH - 10, random.randint(0, constants._SCREEN_HEIGHT)]
        self.computer_list.append(wall)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.computer_list = arcade.SpriteList(use_spatial_hash=True)

        # Set up the player, specifically placing it at these coordinates.
        image_source = ":resources:images/animated_characters/male_person/malePerson_jump.png"
        self.player_sprite = arcade.Sprite(image_source, constants._CHARACTER_SCALING)
        self.player_sprite.center_x = constants._SCREEN_WIDTH / 2
        self.player_sprite.center_y = constants._SCREEN_HEIGHT / 2
        self.player_list.append(self.player_sprite)
        self.view_bottom = 0
        self.view_left = 0
        self.score = 0

        arcade.schedule(self.generate_enemy, 1)

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.computer_list.draw()
        self.player_list.draw()
        __score_text = f"Score: {self.score}"
        arcade.draw_text(__score_text, 10 + self.view_left, 10 + self.view_bottom, arcade.csscolor.BLACK, 18)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = constants._PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -constants._PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -constants._PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = constants._PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.eat_sound = arcade.load_sound(":resources:sounds/hit3.wav")
        self.ow_sound = arcade.load_sound(":resources:sounds/lose5.wav")

        self.collided_sprites = arcade.check_for_collision_with_list(self.player_sprite, self.computer_list)

        for sprite in self.collided_sprites:
            player_size = self.player_sprite._get_scale()
            if sprite._get_scale() >= player_size:
                arcade.play_sound(self.ow_sound)
                view = draw.GameOverView()
                self.window.show_view(view)   #Should call upon the end screen
            else:
                new_player_size = self.player_sprite._get_scale() + (sprite._get_scale() / 10)
                self.computer_list.remove(sprite)
                self.player_sprite._set_scale(new_player_size)
                arcade.play_sound(self.eat_sound)
                self.score += 1


        self.player_sprite.center_y += self.player_sprite.change_y
        self.player_sprite.center_x += self.player_sprite.change_x

        for sprite in self.computer_list:
            sprite.center_x += -4
            if sprite._get_center_x() <= 1.0:
                self.computer_list.remove(sprite)