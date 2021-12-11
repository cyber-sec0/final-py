import arcade, random
from zombiekiller import constants, menu

class GameOverView(arcade.View):
    """ Class to manage the game over view"""

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Draw the game over view """
        arcade.start_render()
        arcade.draw_text("Game Over - press ENTER to Restart, ESCAPE to Exit", constants._SCREEN_WIDTH/2, constants._SCREEN_HEIGHT/1.5, arcade.color.WHITE, font_size=30, anchor_y = "top", anchor_x="center")

    def on_key_press(self, key, _modifiers):
        """ If user hits enter, go back to the main menu view, or quit if escape is hit"""
        if key == arcade.key.ENTER:
            __menu_view = menu.MenuView()
            self.window.show_view(__menu_view)
        elif key == arcade.key.ESCAPE:
            self.window.close()
            self.window = None
            return