"""

"""

import random
import arcade

# --- Constants ---
SPRITE_SCALING_ITEM = .75
ITEM_COUNT = 25

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Sprite Collect Coins Example"


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.rock_list = None
        self.paper_list = None
        self.scissors_list = None

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.rock_list = arcade.SpriteList()
        self.paper_list = arcade.SpriteList()
        self.scissors_list = arcade.SpriteList()

        # Create the items
        for i in range(3):
            for j in range(ITEM_COUNT):
                if i == 0:
                    # Create the coin instance
                    # Coin image from kenney.nl
                    item = arcade.Sprite(r"C:\Git projects\PythonGames\RockPaperScissors\Rock.png", SPRITE_SCALING_ITEM, hit_box_algorithm='Simple')

                    # Position the coin
                    item.center_x = random.randrange(SCREEN_WIDTH)
                    item.center_y = random.randrange(SCREEN_HEIGHT)

                    # Add the coin to the lists
                    self.rock_list.append(item)
                elif i == 1:
                    # Create the coin instance
                    # Coin image from kenney.nl
                    item = arcade.Sprite(r"C:\Git projects\PythonGames\RockPaperScissors\Paper.png", SPRITE_SCALING_ITEM)

                    # Position the coin
                    item.center_x = random.randrange(SCREEN_WIDTH)
                    item.center_y = random.randrange(SCREEN_HEIGHT)

                    # Add the coin to the lists
                    self.paper_list.append(item)
                elif i == 2:
                    # Create the coin instance
                    # Coin image from kenney.nl
                    item = arcade.Sprite(r"C:\Git projects\PythonGames\RockPaperScissors\Scissors.png", SPRITE_SCALING_ITEM)

                    # Position the coin
                    item.center_x = random.randrange(SCREEN_WIDTH)
                    item.center_y = random.randrange(SCREEN_HEIGHT)

                    # Add the coin to the lists
                    self.scissors_list.append(item)

    def on_draw(self):
        """ Draw everything """
        self.clear()
        self.rock_list.draw()
        self.paper_list.draw()
        self.scissors_list.draw()


def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
'''
import arcade
import random

item_type = ['Rock', 'Paper', 'Scissors']
WIDTH = 400
HEIGHT = 600
TITLE = 'Rock vs Paper vs Scissors'
NUMBER_OF_ITEMS = 30


class Item:
    # class variables
    max_rocks = 10
    max_papers = 10
    max_scissors = 10

    # class methods
    def __init__(self, x_pos, y_pos, delta_x, delta_y, itm_type):
        """
        initial values for class instance variables
        :param x_pos: position of the item on the x axis
        :param y_pos: position of the item on the y axis
        :param itm_type: can be Rock, Paper or Scissors
        :return:
        """
        self.x = x_pos
        self.y = y_pos
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.item_type = itm_type

    def move(self):
        if self.x >= WIDTH:
            self.x = WIDTH - 2
        elif self.x <= 0:
            self.x = 2
        else:
            self.x += (random.choice([-1, 1]) * Item.move_speed)

        if self.y >= HEIGHT:
            self.y = HEIGHT - 2
        elif self.y <= 0:
            self.y = 2
        else:
            self.y += (random.choice([-1, 1]) * self.move_speed)


class MyGame(arcade.Window):
    """ Main application class. """
    def __init__(self):
        # Call the parent __init__
        super().__init__(WIDTH, HEIGHT, TITLE)

        # Create a item list
        self.item_list = []

        for i in range(NUMBER_OF_ITEMS):

            # Random spot
            x = random.randrange(0, WIDTH)
            y = random.randrange(0, HEIGHT)

            i_type = random.randrange(3)

            item = Item(x, y, item_type[i_type])

            # Add this new shape to the list
            self.item_list.append(item)

    def on_update(self, dt):
        """ Move everything """
        for item in self.item_list:
            item.move()

    def on_draw(self):
        """ Render the screen. """

        # Clear teh screen
        self.clear()

        # Draw the shapes
        for item in self.item_list:
            item.draw()


def main():
    MyGame()
    arcade.run()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()'''
