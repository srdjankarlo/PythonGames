"""

"""

import random
import arcade

# --- Constants ---
SPRITE_SCALING_ITEM = .75
ITEM_COUNT = 40

SCREEN_WIDTH = 350
SCREEN_HEIGHT = 550
SCREEN_TITLE = "Rock vs Paper vs Scissors"

images = [r"C:\Git projects\PythonGames\RockPaperScissors\Rock.png",
          r"C:\Git projects\PythonGames\RockPaperScissors\Paper.png",
          r"C:\Git projects\PythonGames\RockPaperScissors\Scissors.png"]


class Item(arcade.Sprite):

    def __init__(self, filename, sprite_scaling, tip):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0
        self.item_type = tip

    def update(self):

        # Move the item
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 50:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.all_sprite_list = None
        self.rock_list = None
        self.paper_list = None
        self.scissors_list = None

        self.item_sprite = None

        # scores
        self.r_score = 0
        self.p_score = 0
        self.s_score = 0

        arcade.set_background_color(arcade.color.WHITE_SMOKE)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.all_sprite_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()
        self.paper_list = arcade.SpriteList()
        self.scissors_list = arcade.SpriteList()

        self.r_score = 0
        self.p_score = 0
        self.s_score = 0

        # Create the items
        for i in range(3):
            for j in range(ITEM_COUNT):
                if i == 0:
                    # Create the rock instance
                    # Rock image
                    self.item_sprite = Item(images[0], SPRITE_SCALING_ITEM, 'r')

                    self.r_score += 1

                    # Position the rock
                    self.item_sprite.center_x = random.randrange(SCREEN_WIDTH)
                    self.item_sprite.center_y = random.randrange(50, SCREEN_HEIGHT)
                    dx = random.randrange(-2, 2)
                    if dx == 0:
                        dx = 1
                    dy = random.randrange(-2, 2)
                    if dy == 0:
                        dy = 1
                    self.item_sprite.change_x = dx
                    self.item_sprite.change_y = dy

                    # Add the rock to the lists
                    self.all_sprite_list.append(self.item_sprite)
                    self.rock_list.append(self.item_sprite)
                elif i == 1:
                    self.item_sprite = Item(images[1], SPRITE_SCALING_ITEM, 'p')
                    self.p_score += 1

                    self.item_sprite.center_x = random.randrange(SCREEN_WIDTH)
                    self.item_sprite.center_y = random.randrange(50, SCREEN_HEIGHT)
                    dx = random.randrange(-2, 2)
                    if dx == 0:
                        dx = 1
                    dy = random.randrange(-2, 2)
                    if dy == 0:
                        dy = 1
                    self.item_sprite.change_x = dx
                    self.item_sprite.change_y = dy

                    self.all_sprite_list.append(self.item_sprite)
                    self.paper_list.append(self.item_sprite)
                elif i == 2:
                    self.item_sprite = Item(images[2], SPRITE_SCALING_ITEM, 's')
                    self.s_score += 1

                    self.item_sprite.center_x = random.randrange(SCREEN_WIDTH)
                    self.item_sprite.center_y = random.randrange(50, SCREEN_HEIGHT)
                    dx = random.randrange(-2, 2)
                    if dx == 0:
                        dx = 1
                    dy = random.randrange(-2, 2)
                    if dy == 0:
                        dy = 1
                    self.item_sprite.change_x = dx
                    self.item_sprite.change_y = dy

                    self.all_sprite_list.append(self.item_sprite)
                    self.scissors_list.append(self.item_sprite)

    def on_draw(self):
        """ Draw everything """
        self.clear()
        self.all_sprite_list.draw()
        self.rock_list.draw()
        self.paper_list.draw()
        self.scissors_list.draw()

        output = f"Rocks: {self.r_score} Papers: {self.p_score} Scissors: {self.s_score}"
        arcade.draw_text(output, 10, 10, arcade.color.BLACK, 15)

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this example though.)
        self.all_sprite_list.update()

        # delete ones that are hit
        for p in self.paper_list:
            r_hit_list = arcade.check_for_collision_with_list(p, self.rock_list)
            for rock in r_hit_list:
                rock.remove_from_sprite_lists()

                # added code to change rock to paper
                # center_x = rock.center_x
                # center_y = rock.center_y
                # change_x = rock.change_x
                # change_y = rock.change_y
                # self.item_sprite = Item(images[0], SPRITE_SCALING_ITEM, 'p')
                # self.item_sprite.center_x = center_x
                # self.item_sprite.center_y = center_y
                # self.item_sprite.change_x = change_x
                # self.item_sprite.change_y = change_y
                # self.all_sprite_list.append(self.item_sprite)
                # self.paper_list.append(self.item_sprite)

                self.r_score -= 1
                # self.p_score += 1

        for s in self.scissors_list:
            p_hit_list = arcade.check_for_collision_with_list(s, self.paper_list)
            for paper in p_hit_list:
                paper.remove_from_sprite_lists()
                # center_x = paper.center_x
                # center_y = paper.center_y
                # change_x = paper.change_x
                # change_y = paper.change_y
                # self.item_sprite = Item(images[0], SPRITE_SCALING_ITEM, 's')
                # self.item_sprite.center_x = center_x
                # self.item_sprite.center_y = center_y
                # self.item_sprite.change_x = change_x
                # self.item_sprite.change_y = change_y
                # self.all_sprite_list.append(self.item_sprite)
                # self.scissors_list.append(self.item_sprite)
                self.p_score -= 1
                # self.s_score += 1

        for r in self.rock_list:
            s_hit_list = arcade.check_for_collision_with_list(r, self.scissors_list)
            for scissors in s_hit_list:
                scissors.remove_from_sprite_lists()
                # center_x = scissors.center_x
                # center_y = scissors.center_y
                # change_x = scissors.change_x
                # change_y = scissors.change_y
                # self.item_sprite = Item(images[0], SPRITE_SCALING_ITEM, 'r')
                # self.item_sprite.center_x = center_x
                # self.item_sprite.center_y = center_y
                # self.item_sprite.change_x = change_x
                # self.item_sprite.change_y = change_y
                # self.all_sprite_list.append(self.item_sprite)
                # self.rock_list.append(self.item_sprite)
                self.s_score -= 1
                # self.r_score += 1


def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
