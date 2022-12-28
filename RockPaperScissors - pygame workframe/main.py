import pygame
import time
import os
import random
import keyboard

pygame.font.init()

WIN_WIDTH = 500
WIN_HEIGHT = 600

ITEM_IMGS = [pygame.image.load(os.path.join("imgs", "rock.png")),
             pygame.image.load(os.path.join("imgs", "paper.png")),
             pygame.image.load(os.path.join("imgs", "scissors.png"))]
BG_IMG = pygame.image.load(os.path.join("imgs", "background.png"))
NUM_OF_ITEMS = 30
STAT_FONT = pygame.font.SysFont("comicsans", 20)


class Item:
    def __init__(self, x, y, img, itm_type):
        self.x = x
        self.y = y
        self.img = img
        self.item_type = itm_type

    def move(self):
        self.y += random.randrange(-5, 6)
        self.x += random.randrange(-5, 6)

        if self.y >= 450:
            self.y = 450
        elif self.y <= 50:
            self.y = 50

        if self.x >= 450:
            self.x = 450
        elif self.x <= 50:
            self.x = 50

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

    def collide(self, other_item):
        other_item_mask = other_item.get_mask()
        item_mask = pygame.mask.from_surface(self.img)
        other_item_offset = (self.x - other_item.x, self.y - other_item.y)
        point = other_item_mask.overlap(item_mask, other_item_offset)

        if point:
            return True
        return False


def draw_window(win, items, score_r, score_p, score_s):
    win.blit(BG_IMG, (0, 0))  # blit means draw, (0,0) je na topleft poziciji ekrana

    for item in items:
        item.draw(win)

    text = STAT_FONT.render("Rocks: " + str(score_r) +
                            " Papers: " + str(score_p) +
                            " Scissors: " + str(score_s),
                            True, (0, 0, 0))
    win.blit(text, (0, WIN_HEIGHT - 115))  # iscrtaj text sa zadatim x i y koordinatama

    pygame.display.update()  # updates display


def main():
    # starting values for items
    items = []
    score_r = NUM_OF_ITEMS
    score_p = NUM_OF_ITEMS
    score_s = NUM_OF_ITEMS
    text = ''
    # make items
    for item in range(NUM_OF_ITEMS):
        items.append(Item(random.randrange(80, 250), random.randrange(230, 420), ITEM_IMGS[0], 'ROCK'))
        items.append(Item(random.randrange(165, 335), random.randrange(50, 220), ITEM_IMGS[1], 'PAPER'))
        items.append(Item(random.randrange(250, 420), random.randrange(250, 420), ITEM_IMGS[2], 'SCISSORS'))

    win = pygame.display.set_mode(
        (WIN_WIDTH, WIN_HEIGHT))  # kreirali objekat windowsa gde ce biti igrica, u sustini ekran na kom se igra igra

    clock = pygame.time.Clock()  # ovo implementiramo da tica ne bi pala odmah kad se pokrene igra, set the frame rate of the loop

    run = True
    while run:
        for event in pygame.event.get():  # kad god se nesto desi, npr korisnik klikne misem
            if event.type == pygame.QUIT:  # ako pritisnemo crveni iks u gornjem desnom uglu
                run = False  # izlazi iz petlje
                pygame.quit()  # izlazi iz pygame
                quit()  # izlazi iz programa

        clock.tick(30)
        for event in pygame.event.get():  # kad god se nesto desi, npr korisnik klikne misem
            if event.type == pygame.QUIT:  # ako pritisnemo crveni iks u gornjem desnom uglu
                run = False  # izlazi iz petlje

        # check collisions
        for item1 in items:
            for item2 in items:
                if item2.collide(item1):
                    if item2.item_type == 'ROCK' and item1.item_type == 'PAPER':
                        score_r -= 1
                        # items.remove(item2)
                        item2.item_type = 'PAPER'
                        item2.img = ITEM_IMGS[1]
                        score_p += 1
                    elif item2.item_type == 'PAPER' and item1.item_type == 'SCISSORS':
                        score_p -= 1
                        # items.remove(item2)
                        item2.item_type = 'SCISSORS'
                        item2.img = ITEM_IMGS[2]
                        score_s += 1
                    elif item2.item_type == 'SCISSORS' and item1.item_type == 'ROCK':
                        score_s -= 1
                        # items.remove(item2)
                        item2.item_type = 'ROCK'
                        item2.img = ITEM_IMGS[0]
                        score_r += 1

        # move the items
        for item in items:
            item.move()

        if score_r >= 0 and score_p == 0 and score_s >= 0:
            text = 'Rock wins'
            run = False
        elif score_r >= 0 and score_p >= 0 and score_s == 0:
            text = 'Paper wins'
            run = False
        elif score_r == 0 and score_p >= 0 and score_s >= 0:
            text = 'Scissors wins'
            run = False

        draw_window(win, items, score_r, score_p, score_s)  # pozivamo metodu

    text = STAT_FONT.render(text, True, (0, 0, 0))
    over = False
    while not over:
        win.blit(text, (0, WIN_HEIGHT - 95))
        gameover = STAT_FONT.render("Restar? (y/n)!", True, (0, 0, 0))
        # rect = gameover.get_rect()
        # rect.center = win.get_rect().center
        # win.blit(BG_IMG, (0, 0))
        win.blit(gameover, (0, WIN_HEIGHT - 75))
        pygame.display.update()

        for event in pygame.event.get():  # kad god se nesto desi, npr korisnik klikne misem
            if event.type == pygame.QUIT:  # ako pritisnemo crveni iks u gornjem desnom uglu
                over = True  # izlazi iz petlje
                pygame.quit()  # izlazi iz pygame
                quit()  # izlazi iz programa
        
        for event in pygame.event.get():  # kad god se nesto desi, npr korisnik klikne misem
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    main()
                elif event.key == pygame.K_n:
                    over = True
                    run = False

    pygame.quit()  # izlazi iz pygame
    quit()  # izlazi iz programa


main()
