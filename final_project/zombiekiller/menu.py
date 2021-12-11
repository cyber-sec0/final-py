import arcade
from zombiekiller import constants, music

class MenuView(arcade.View):
    """ Class that manages the 'menu' view"""

    def on_show(self):
        """ Called when switching to this view"""
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.WHITE)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, constants._SCREEN_WIDTH - 1, 0, constants._SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_text("Welcome to ZOMBIE KILLER! \n\n", constants._SCREEN_WIDTH/2, constants._SCREEN_HEIGHT/1.5, arcade.color.BLACK, font_size=55, anchor_y = "top", anchor_x ="center")
        arcade.draw_text("Kill/Run using WASD, kill the smaller zombies to get stronger, run from the bigger zombies or you'll die. Click anywhere to start.", constants._SCREEN_WIDTH/2, constants._SCREEN_HEIGHT/2, arcade.color.BLACK, font_size=15, anchor_y = "center", anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Use a mouse press to advance to the 'game' view"""
        __game_view = music.MyGame(arcade.View, self)
        __game_view.setup()
        self.window.show_view(__game_view)
